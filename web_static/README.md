# AirBnB Clone - Web Static

This project is the first step in building an AirBnB clone. It focuses on creating static HTML pages with CSS styling to design and prototype the frontend interface.

## Project Description

The goal of this project is to learn how to manipulate HTML and CSS to create a web page structure and design. This project includes:

- Creating simple HTML static pages
- Implementing a style guide
- Using fake content (no JavaScript or dynamic data)
- Progressive development from inline styles to external CSS files
- Creating responsive layouts and interactive elements (hover effects)

## Learning Objectives

By completing this project, you will understand:

- What HTML is and how to create an HTML page
- What a markup language is
- What the DOM (Document Object Model) is
- What elements/tags and attributes are
- How browsers load webpages
- What CSS is and how to add styles to elements
- What classes and selectors are
- How to compute CSS Specificity Value
- What Box properties are in CSS

## Requirements

- All files must end with a new line
- Code must be W3C compliant and validate with W3C-Validator
- All CSS files must be in the `styles` folder
- All images must be in the `images` folder
- No use of `!important` or `id` in CSS files
- No use of `<img>`, `<embed>`, or `<iframe>` tags
- No JavaScript allowed
- Tested on Chrome 56 or later

## Project Structure

```
alu-AirBnB_clone/
└── web_static/
    ├── 0-index.html          # Inline styling
    ├── 1-index.html          # Head styling
    ├── 2-index.html          # External CSS files
    ├── 3-index.html          # Zoning with header/footer styling
    ├── 4-index.html          # Search filters
    ├── 5-index.html          # More filters
    ├── 6-index.html          # Dropdown filters
    ├── 7-index.html          # Display results
    ├── 8-index.html          # More details
    ├── styles/
    │   ├── 2-common.css
    │   ├── 2-header.css
    │   ├── 2-footer.css
    │   ├── 3-common.css
    │   ├── 3-header.css
    │   ├── 3-footer.css
    │   ├── 4-common.css
    │   ├── 4-filters.css
    │   ├── 5-filters.css
    │   ├── 6-filters.css
    │   ├── 7-places.css
    │   └── 8-places.css
    └── images/
        ├── icon.png
        ├── logo.png
        ├── icon_group.png
        ├── icon_bed.png
        └── icon_bath.png
```

## Tasks

### 0. Inline styling
Write an HTML page with a header and footer using inline styling.

### 1. Head styling
Same as task 0, but using the `<style>` tag in the `<head>` section.

### 2. CSS files
Same as task 1, but using external CSS files.

### 3. Zoning done!
Add proper styling with custom fonts, colors, and a logo.

### 4. Search!
Add a filters section with a search button.

### 5. More filters
Add location and amenities filters.

### 6. It's (h)over
Add dropdown menus that appear on hover.

### 7. Display results
Add a places section to display search results.

### 8. More details
Add detailed information to each place (price, guests, rooms, bathrooms, owner, description).

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/alu-AirBnB_clone.git
cd alu-AirBnB_clone/web_static
```

2. Add the required images to the `images/` folder:
   - `icon.png` - Favicon for the browser tab
   - `logo.png` - AirBnB logo for the header
   - `icon_group.png` - Icon for guest count
   - `icon_bed.png` - Icon for bedroom count
   - `icon_bath.png` - Icon for bathroom count

3. Open any HTML file in your browser:
```bash
# On Ubuntu WSL, you can use:
explorer.exe 0-index.html
# Or
google-chrome 0-index.html
# Or
firefox 0-index.html
```

## Validation

To validate your HTML and CSS:

1. Visit [W3C HTML Validator](https://validator.w3.org/)
2. Upload your HTML file or paste the code
3. Fix any errors or warnings

For CSS validation:
1. Visit [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
2. Upload your CSS file or paste the code
