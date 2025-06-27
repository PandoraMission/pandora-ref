# Pandora Reference

This package is a repository to hold reference data for the Pandora SmallSat data processing. This repository is **only used to store the current best reference products** for Pandora data processing. Rolling back to previous versions of this package will roll back to previous versions of reference products. All processed products will contain a version number of this package, which links to specific versions of processing files. At any given version number there is a single version of each file.

Follow this README strictly when updating products.

## Updating any number of reference products

If you are going to update reference products for Pandora processing you must follow these steps.

1. Clone this repository, if you do not already have a copy
2. Ensure the repository is up to date (`git pull`)
3. Go to the specific product within `src/pandoraref/data/` that you wish to update.

- Verify that your new product is compliant with the fits file format of the original product. (Note: If you change the format (e.g. add or remove headers or extensions), you must update the minor version number of this package.)
- Ensure your new product has an incremented version number in the header, compared to the old product.
- If you are changing the file name, ensure the new product follows the file naming convention.

4. Replace the file in the `src/pandoraref/data/`.
5. Where appropriate, update the README for each file.
6. In this modules `__init__.py` file, ensure that the product name is correct in the loading class. If you have added a new file or changed a name, make sure to update the class.
7. In this modules `pyproject.py` file update the version number. Follow the rules below.
8. Update the CHANGELOG for this package.

You may update multiple data products at once, but if you make any changes to this repository you must update the version number of this package.

### Versioning

Version numbers appear in two places:

1. Each file should have its own, consistent version number. If you update a flat field, you should increment the version number in that file.
2. The package itself represents the full assembly of the reference data products. If any files within the system change, this must be incremented.

When processing Pandora data, refer to the `pandora-ref` package number that was used when processing, so that your processing is reproducible using the same exact set of reference files.

If a file has a version name `dummy` this means this is a file that is for format definition only, and is not meant to be used in practice. `dummy` files should still be in the correct format, and should have data in them so that they can be applied (e.g. a flat field of 1's, a bias value of 0) but they should not contain any real information or expectations.

Follow this convention when updating the package version number

- Updating information within this package (e.g. readmes, docstrings): update patch number
- Updating data within files, but not changing any file structure: update patch number
- Updating data and changing the file structure (e.g. adding or removing headers or extensions): update minor version number
- Adding or removing data products entirely: update major version number

## Contents

For any given version number this package will have a single file for at least these files for both Pandora detectors

- Flat field
- Bias image
- Dark image
- Gain setting
- Read noise estimates
- Bad pixel map
- Non linearity curve
- PSF model
- WCS parameters
- WCS distortion
- Quantum Efficiency
- Throughput

For NIRDA only there will be a single file for

- Wavelength as a function of pixel position (as measured)

### Future contents

It's expected that this repository will eventually include some number of SPICE kernels, and potentially will download and store locally the most recent SPICE kernels for the mission.

## Usage

If you use this package as a dependency to process data, follow these guidelines:

**I want to have my processing be reproducible**

In this case you should set the dependency to a specific stable version of `pandora-ref`. In any product you make you should specify the exact version number of `pandora-ref` you use.

**I want to have my processing have the best possible reference data**

In this case you should set the dependency to a specific major and minor versino of `pandora-ref`, but you can enable any patch number and pull the latest patches any time you run. You should keep any eye out for major or minor package version updates. In the case that there is a major or minor version update you should pull these updates, but you may need to update your code base as the file structures may have changed or new files may have been added. In any product you make you should specify the exact version number of `pandora-ref` you use.

### Installing and importing this package

You can install this package with pip. Once you install it as a dependency you will have the reference files installed locally. You can then find each file using the reference path objects:

```python
from pandoraref import NIRDAReference
nirdaref = NIRDAReference()

nirdaref.flat_file
nirdaref.badpix_file
```

These will each return strings. You can open the files astropy's FITS module

```python
from pandoraref import NIRDAReference
from astropy.io import fits
nirdaref = NIRDAReference()

with fits.open(nirdaref.flat_file) as hdulist:
    print(hdulist[0].header['VERSION'])
```

### Function naming

In this package (and all packages) names matter. We follow this naming convention wherever we can:

- Lower case noun is a property, e.g. `flat_file` is a property which is a string
- Lower case verb and then noun is a function e.g. `get_flat_file` would be a function

Certain verbs imply actions:

- `get_` implies retrieve and return an object. e.g. `get_wcs` will retrieve a WCS from storage and return that object.
- `create_` implies it will generatea new object, rather than `get`ting one from file e.g. `create_wcs` will create a new WCS solution from scratch

## What should be stored in this package?

This package is **not** the place to put codes, processes or data that **generates** reference data products.

This package is to

1. Store current best estimates of reference products
2. Hold functions to **convert** between data between other formats and the expected RDP format. (e.g. if LLNL provided a distortion file as a csv it is allowable to store that CSV and have a function to **convert** it to an expected fits file.)
3. Hold functions to return versions of RDPs under specific conditions. For example, a function to give the WCS RDP given an expected pointing.

Do not store calibration data or any generation scripts here.
