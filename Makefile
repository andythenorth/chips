# Various needed programs
GIT = git
PYTHON3 = python3
SED = sed
ZIP = zip

GRFCODEC = grfcodec
GRFID = grfid

NFORENUM = nforenum
NFORENUM_FLAGS ?= $(shell [ `$(NFORENUM) -s -v 2>/dev/null | wc -l ` -eq 1 ] && echo "-s" || echo "")
NFO_WARN_LEVEL ?= 4

CC             ?= gcc
CC_FLAGS       ?= -C -E -nostdinc -x c-header - <

GIT_INFO = $(PYTHON3) src/polar_fox/git_info.py
FILL_TEMPLATE = bin/fill-template
FIND_FILES = bin/find-files
MK_ARCHIVE = bin/mk-archive


# Project details
PROJECT_NAME = chips

EXPORTED = no
ifeq ($(strip $(EXPORTED)),no)
  # Not exported source, therefore regular checkout
  REPO_INFO = $(shell $(GIT_INFO))
  REPO_REVISION = $(word 1,$(REPO_INFO))
  REPO_VERSION = $(word 2,$(REPO_INFO))
else
  # Exported version, lines below should get modified in 'bundle_src' target
  REPO_REVISION = ${exported_revision}
  REPO_VERSION = ${exported_version}
endif

REPO_TITLE = "$(PROJECT_NAME) $(REPO_VERSION)"
REPO_TITLE = "$(PROJECT_NAME)"
PROJECT_VERSIONED_NAME = $(PROJECT_NAME)-$(REPO_VERSION)
ARGS = '$(REPO_REVISION)' '$(REPO_VERSION)'

NFO_FILE = generated/$(PROJECT_NAME).nfo
GRF_FILE = generated/$(PROJECT_NAME).grf
TAR_FILE = $(PROJECT_VERSIONED_NAME).tar
ZIP_FILE = $(PROJECT_VERSIONED_NAME).zip
MD5_FILE = $(PROJECT_NAME).check.md5

SOURCE_NAME = $(PROJECT_VERSIONED_NAME)-source
BUNDLE_DIR = bundle_dir

# Build rules
.PHONY: default grf tar bundle_tar bundle_zip bundle_src clean
default: grf
# bundle needs to clean first to ensure we don't use outdated/cached version info
bundle_tar: clean tar
bundle_zip: $(ZIP_FILE)
nfo: $(NFO_FILE)
grf: $(GRF_FILE)
tar: $(TAR_FILE)

# remove the @ for more verbose output (@ suppresses command output)
_V ?= @

$(NFO_FILE): $(shell $(FIND_FILES) --ext=.pnfo --ext=.tnfo src)
	$(_V) echo "[RENDER NFO]"
	$(_V) if [ ! -d generated ];\
		then mkdir generated;\
	fi;
	$(CC) $(CC_FLAGS) src/chips.pnfo > $(NFO_FILE) > $(NFO_FILE)
	$(_V) $(NFORENUM) $(NFORENUM_FLAGS) $(NFO_FILE)
# renum leaves unwanted .bak file, remove it
	$(_V)  rm -r $(NFO_FILE).bak

# N.B grf codec can't compile into a specific target dir, so after compiling, move the compiled grf to appropriate dir
$(GRF_FILE): $(NFO_FILE) $(shell $(FIND_FILES) --ext=.png src)
	$(_V) echo "[ENCODE GRF]"
	$(GRFCODEC) -s -e -c -n -g 2 $(PROJECT_NAME).grf generated
	$(_V) mv $(PROJECT_NAME).grf $(GRF_FILE)

$(TAR_FILE): $(GRF_FILE)
# the goal here is a sparse tar that bananas will accept; bananas can't accept html docs etc, hence they're not included
# create an intermediate dir, and copy in what we need for bananas
	$(_V) echo "[CREATE BUNDLE TAR]"
	$(_V) mkdir $(PROJECT_VERSIONED_NAME)
	$(_V) echo "[...COPYING DOCS...]"
	$(_V) cp docs/readme.txt $(PROJECT_VERSIONED_NAME)
	$(_V) cp docs/license.txt $(PROJECT_VERSIONED_NAME)
	$(_V) cp docs/changelog.txt $(PROJECT_VERSIONED_NAME)
	$(_V) echo "[...COPYING GRF...]"
	$(_V) cp $(GRF_FILE) $(PROJECT_VERSIONED_NAME)
	$(_V) echo "[...COMPRESSING...]"
	$(_V) $(MK_ARCHIVE) --tar --output=$(TAR_FILE) --base=$(PROJECT_VERSIONED_NAME) $(PROJECT_VERSIONED_NAME)
# delete the intermediate dir
	$(_V) rm -r $(PROJECT_VERSIONED_NAME)
	$(_V) echo "[DONE]"

$(ZIP_FILE): $(TAR_FILE)
	$(ZIP) -9rq $(ZIP_FILE) $(TAR_FILE) >/dev/null

$(MD5_FILE): $(GRF_FILE)
	$(GRFID) -m $(GRF_FILE) > $(MD5_FILE)

bundle_src: $(MD5_FILE)
	if test -d $(BUNDLE_DIR); then rm -r $(BUNDLE_DIR); fi
	mkdir $(BUNDLE_DIR)
	$(GIT) archive -t files $(BUNDLE_DIR)/src
	$(FILL_TEMPLATE) --template=Makefile \
		--output=$(BUNDLE_DIR)/src/Makefile \
		"exported_revision=$(REPO_REVISION)" \
		"exported_version=$(REPO_VERSION)"
	$(SED) -i -e 's/^EXPORTED = no/EXPORTED = yes/' $(BUNDLE_DIR)/src/Makefile
	$(MK_ARCHIVE) --tar --output=$(SOURCE_NAME).tar --base=$(SOURCE_NAME) \
		`$(FIND_FILES) $(BUNDLE_DIR)/src` $(MD5_FILE)

# this is a macOS-specifc install location; the pre-2017 Makefile handled multiple platforms, that could be restored if needed
# remove first, OpenTTD does not like having the _contents_ of the current file change under it, but will handle a removed-and-replaced file correctly
install: default
	rm ~/Documents/OpenTTD/newgrf/$(PROJECT_NAME).grf
	cp $(GRF_FILE) ~/Documents/OpenTTD/newgrf/

clean:
	$(_V) echo "[CLEANING]"
	$(_V) for f in $(NFO_FILE) $(GRF_FILE) generated $(TAR_FILE) $(ZIP_FILE) $(MD5_FILE) $(BUNDLE_DIR) $(SOURCE_NAME).tar;\
	do if test -e $$f;\
	   then rm -r $$f;\
	   fi;\
	done
	$(_V) echo "[DONE]"
