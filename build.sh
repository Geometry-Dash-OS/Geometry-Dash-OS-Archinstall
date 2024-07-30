cd ./pkg/
rm -rf src
rm -rf src
cd ..
python -m build --wheel --no-isolation
python -m installer --destdir=pkg dist/*.whl
cd ./pkg/
mkdir src
mv ./usr/ ./src/
makepkg -s

