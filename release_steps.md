# Steps to update on GitHub and PyPi

I forget how to do this, so here is a reference for me. This is based on this [post](http://peterdowns.com/posts/first-time-with-pypi.html).

## The process

- Make necessary changes.
- Test.
- Increment version in:
    * setup.py (version and download url)
    * CHANGES.txt
    * ./tiffcapture/__init__.py
- Commit to Git.
- Tag new release, e.g.
    * git tag 0.1.6 -m "PyPi: Change description"
- Push new version to GitHub:
    * git push 
    * git push --follow-tags
- Push new version to PyPi testing: 
    * python setup.py register -r pypitest
    * python setup.py sdist upload -r pypitest
    * visit https://testpypi.python.org/pypi/TiffCapture to confirm
- Push new version to PyPi real:
    * python setup.py register -r pypi
    * python setup.py sdist upload -r pypi
    * visit https://pypi.python.org/pypi/TiffCapture to confirm


