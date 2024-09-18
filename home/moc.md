# Ashrei Wellness Directory structure
 home
├──  app.css                                # Main application styles
├──  assets                                 # Static assets directory
│  ├── [various SVG and image files]         # Icons and images used throughout the site
│  ├──  fonts                               # Custom font files
│  └──  icons                               # Additional icon assets
|
├──  card3d.css                             # Styles for 3D card effect
├──  card3d.js                              # JavaScript for 3D card functionality
├──  content.py                             # Defines content, sample data, and component demos
|
├──  css
│  ├──  highlighter-theme.css               # Syntax highlighting styles for code snippets
│  ├──  input.css                           # Styles for input elements
│  ├──  main.css                            # Main CSS file, likely imports other CSS files
│  ├──  preview-stack.css                   # Styles for preview stack component
│  ├──  stack.css                           # Styles for stack component
│  └──  tailwind.css                        # Compiled Tailwind CSS styles
|
├──  data                                   # Database files for todo app demo
│  ├──  todos.db
│  ├──  todos.db-shm
│  └──  todos.db-wal
|
├──  favicon-dark.ico                       # Dark mode favicon
├──  favicon.ico                            # Light mode favicon
├──  FRONTEND_HANDOVER.md                   # Documentation for frontend developers
├──  home_components.py                     # Defines reusable UI components and utility functions
|
├──  js
│  ├──  carouselScroll.js                   # JavaScript for carousel scrolling
│  ├──  codeOverflow.js                     # Handles code snippet overflow
│  ├──  copyCode.js                         # Functionality to copy code snippets
│  ├──  index.js                            # Main JavaScript file, likely imports other JS files
│  ├──  previewStack.js                     # JavaScript for preview stack component
│  ├──  pythonHighlighter.js                # Custom syntax highlighter for Python
│  ├──  stack.js                            # JavaScript for stack component
│  ├──  togglePreview.js                    # Handles toggling of preview elements
│  └──  videoPopup.js                       # JavaScript for video popup functionality
|
├──  main-console.ipynb                     # Jupyter notebook for development/testing
├──  main.py                                # Main entry point for the FastHTML application
├──  README.md                              # Project overview and documentation
├──  requirements.txt                       # Python dependencies for the project
├──  tailwind.config.js                     # Configuration file for Tailwind CSS
└──  weather.py                             # Weather-related functionality (not shown in provided code)


Key interactions:

1. `main.py` is the central file that imports components from `home_components.py` and content from `content.py`.

2. `content.py` defines sample data and component demos used in `main.py`.

3. CSS files in the `css` directory are likely imported in `main.css` and referenced in `main.py` for styling.

4. JavaScript files in the `js` directory are included in `main.py` and interact with the DOM elements defined in the Python code.

5. `home_components.py` defines reusable UI components used throughout `main.py`.

6. `tailwind.config.js` configures Tailwind CSS, which is compiled into `css/tailwind.css`.

7. Assets in the `assets` directory are referenced in the HTML generated by the Python code.

8. `FRONTEND_HANDOVER.md` provides documentation for frontend developers, explaining the structure and special elements used in the HTML.

Ashrei Wellness is a FastHTML application with a mix of Python for server-side rendering, JavaScript for client-side interactivity, and CSS for styling, all working together to create a responsive and dynamic website.
---

Certainly! We'll create a map of content with detailed descriptions for the Ashrei Wellness project, focusing on the home directory. This will help you understand the structure and purpose of each file, especially considering your familiarity with Python and newness to JavaScript, CSS, and HTML.

# Ashrei Wellness Project Structure

## /home
This is the main directory for the Ashrei Wellness website.

### Python Files

1. **main.py**
   - Main entry point for the FastHTML application
   - Defines routes, page structures, and imports components
   - Key file for understanding the overall structure of the web application

2. **content.py**
   - Contains content-related functions and data
   - Defines sample data, weather table placeholder, and component demos
   - Useful for managing dynamic content across the site

3. **home_components.py**
   - Defines reusable UI components and utility functions
   - Contains common CSS classes and layout helpers
   - Important for understanding how the UI is structured

4. **weather.py** (not shown in the provided code)
   - Likely contains weather-related functionality

### JavaScript Files

1. **js/index.js**
   - Main JavaScript file for the website
   - Handles various interactive elements like tabs, code highlighting, and carousel functionality
   - Key file for understanding client-side interactions

2. **js/togglePreview.js**
   - Manages the toggling of preview elements in the UI
   - Handles tab switching and highlighting

3. **card3d.js**
   - Implements 3D card effect functionality
   - Uses mouse/touch events for interactive card rotation

4. **tailwind.config.js**
   - Configuration file for Tailwind CSS
   - Defines content sources and any theme extensions

### CSS Files

1. **css/main.css**
   - Main CSS file for custom styles
   - Defines typography, animations, and custom utility classes

2. **css/highlighter-theme.css**
   - Styles for code syntax highlighting

3. **css/stack.css**
   - Styles for stacked card components

4. **card3d.css**
   - Styles specific to the 3D card effect

5. **app.css**
   - Imports Tailwind CSS utilities

### Markdown Files

1. **README.md**
   - Project overview and documentation

2. **FRONTEND_HANDOVER.md**
   - Documentation for frontend developers
   - Explains special IDs, classes, and structure of the HTML

3. **copy.md**
   - Contains website copy and content
   - Includes to-do list and layout thoughts

4. **moc.md**
   - Map of Content file
   - Provides an overview of the project structure (the file you're looking at)

### Other Files

1. **requirements.txt**
   - Lists Python dependencies for the project

2. **favicon.ico** and **favicon-dark.ico**
   - Favicon files for the website

### Directories

1. **assets/**
   - Contains images, icons, and other static assets

2. **css/**
   - Houses CSS files for styling

3. **js/**
   - Contains JavaScript files for client-side functionality

4. **data/**
   - Likely contains database files (e.g., todos.db)

## Key "Knobs" for Customization

1. **Content Customization**:
   - Modify `content.py` to change dynamic content
   - Update `copy.md` for static text content

2. **Styling**:
   - Use `css/main.css` for custom styles
   - Adjust `tailwind.config.js` for Tailwind CSS customizations

3. **Layout and Components**:
   - Modify `home_components.py` to adjust reusable UI components
   - Update `main.py` to change the overall page structure

4. **Interactivity**:
   - Modify `js/index.js` and other JS files in the `js/` directory to adjust client-side behavior

5. **Assets**:
   - Replace or add files in the `assets/` directory for images and icons

By focusing on these files, you can make significant changes to the website's content, appearance, and functionality. Remember to pay special attention to `main.py` as it's the central file tying everything together in the FastHTML framework.