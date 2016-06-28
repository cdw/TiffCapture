from distutils.core import setup

setup(
        name='TiffCapture',
        version='0.1.4',
        author='Dave Williams',
        author_email='cdave@uw.edu',
        packages=['tiffcapture'],
        url='https://github.com/cdw/TiffCapture',
        keywords = ["tiff", "PIL", "OpenCV"],
        classifiers = [
             "Programming Language :: Python",
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: MIT License",
            "Intended Audience :: Science/Research",
            "Operating System :: OS Independent",
            "Topic :: Multimedia :: Graphics",
            "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator"],
        license='LICENSE.txt',
        description="Brings the power of OpenCV to TIFF videos; provides interface to multi-part TIFFs compatible with OpenCV's VideoCapture.",
        long_description=open('README.txt').read(),
        install_requires=["numpy >= 1.8.0", "Pillow >= 2.3.1" ]
)
