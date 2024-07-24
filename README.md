# Vancouver Neighborhood Finder

This Chrome extension allows users to input the first three digits of a Canadian postal code (the FSA - Forward Sortation Area) and receive the corresponding neighborhood name in Vancouver. The extension uses a custom dataset derived from [GeoNames](https://download.geonames.org/export/zip/), modified to fit our specific requirements.

## Features

- Input the first three digits of a Canadian postal code (FSA).
- Get the neighborhood name in Vancouver associated with that FSA.
- Fast and easy lookup directly in your browser.

## Installation

1. Download or clone the repository to your local machine.
2. Open Google Chrome and go to `chrome://extensions/`.
3. Enable "Developer mode" by toggling the switch in the top right corner.
4. Click on "Load unpacked" and select the directory where you downloaded/cloned the repository.
5. The extension should now appear in your list of extensions.

## Usage

1. Click on the extension icon in the Chrome toolbar.
2. Enter the first three digits of the postal code (FSA) in the input field.
3. Press "Submit" to view the neighborhood name.

## Data Source

The neighborhood data is sourced from GeoNames, specifically modified for Vancouver. The original data can be found at [GeoNames Download](https://download.geonames.org/export/zip/).
