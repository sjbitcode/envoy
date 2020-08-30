
1) Install coverage package, and add it to requirements
```
pip install coverage

pip freeze | grep 'requests\|coverage' > requirements.txt
```

2) Run the unit test suite with coverage
```
coverage run --source=envoy -m unittest -v
```

3) Generate the coverage report
```
coverage report --fail-under=90
```
