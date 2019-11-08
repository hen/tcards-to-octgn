sh importer/stage-0-setup/mkdirs.sh
python3 importer/stage-1-get-json/get-json.py
python3 importer/stage-2-build-guids/generate-guid-file.py
python3 importer/stage-3-test-guid-file/test-guid.py
python3 importer/stage-4-test-json-file/test-existing-guids.py
#python3 importer/stage-5-generate-xml-files/generate-sets.py
