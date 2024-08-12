# Project Template

This repository serves as a template for setting up new projects with a consistent structure and style. It includes a basic HTML file, a CSS file for styling, and a Python script for customizing the project.

## Features

- **HTML Template**: A basic `index.html` file with placeholders for project-specific information.
- **CSS Styling**: A `style.css` file with predefined styles and responsive design.
- **Setup Script**: A Python script (`setup.py`) to easily replace placeholders in the HTML file with project-specific values.

## Setup Instructions

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/theEMA-dev/project-template.git
    cd project-template
    ```

2. **Run the Setup Script**:
    ```sh
    python setup.py
    ```
    You will be prompted to enter the following information:
    - Project repository name
    - Initial project name
    - Initial project header

3. **Open the Project**:
    Open the [`index.html`](https://github.com/theEMA-dev/projects-template/blob/main/index.html) file in your browser to see the customized template.

## Usage

- **HTML**: The [`index.html`](https://github.com/theEMA-dev/projects-template/blob/main/index.html) file contains placeholders for the repository name, project name, and project header. These placeholders will be replaced with the values you provide during the setup.
- **CSS**: The [`style.css`](https://github.com/theEMA-dev/projects-template/blob/main/style.css) file includes styles for various elements and supports both light and dark themes.

## Customization

- **HTML**: You can add more content to the [`index.html`](https://github.com/theEMA-dev/projects-template/blob/main/index.html) file as needed. The placeholders `${repoName}`, `${projectName}`, and `${projectNameHeader}` will be replaced with your custom values.
- **CSS**: Modify the [`style.css`](https://github.com/theEMA-dev/projects-template/blob/main/style.css) file to change the styles according to your preferences. The file includes variables for colors, fonts, and other styles.

## Contributing

We welcome contributions to improve this template. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch to your fork.
4. Open a pull request with a description of your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.