pytest -v -s -m "sanity" --html=Reports\sanity.html testCases --browser chrome
@REM pytest -v -s -m "regression" --html=Reports\sanity.html testCases --browser chrome
@REM pytest -v -s -m "sanity and regression" --html=Reports\sanity.html testCases --browser chrome
@REM pytest -v -s -m "sanity or regression" --html=Reports\sanity.html testCases --browser chrome