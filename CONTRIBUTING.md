# Contributing to LogNinja Keylogger

First off, thank you for considering contributing to LogNinja Keylogger! It's people like you that make open-source such a fantastic community.

The following is a set of guidelines for contributing to this project. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to `[INSERT YOUR PROJECT EMAIL HERE]`.

## I don't want to read this whole thing, I just have a question!

> **Note:** Please don't file an issue to ask a question. You'll get faster results by using the resources below.

We have an official discussion place for this project:
*   [GitHub Discussions](https://github.com/sahithuppala05/LogNinja-Keylogger/discussions) - The best place for questions, ideas, and general discussion.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

**Before Submitting A Bug Report**
*   **Check the [existing issues](https://github.com/sahithuppala05/LogNinja-Keylogger/issues)** to see if the problem has already been reported. If it has, add a comment to the existing issue instead of opening a new one.

**How Do I Submit a (Good) Bug Report?**
Bugs are tracked as [GitHub issues](https://github.com/sahithuppala05/LogNinja-Keylogger/issues). Create an issue and provide the following information by filling in the template.

Explain the problem and include additional details to help maintainers reproduce the problem:

*   **Use a clear and descriptive title** for the issue to identify the problem.
*   **Describe the exact steps which reproduce the problem** in as many details as possible.
*   **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
*   **Explain which behavior you expected to see instead and why.**
*   **Include screenshots and animated GIFs** if possible. You can use [LICEcap](https://www.cockos.com/licecap/) to record GIFs on Windows and macOS.
*   **Include your system information** (e.g., OS version, Python version).

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new features and minor improvements to existing functionality.

**Before Submitting An Enhancement Suggestion**
*   **Check if the enhancement has already been suggested** in the [issues list](https://github.com/sahithuppala05/LogNinja-Keylogger/issues).
*   **Use the GitHub Discussions** to see if the idea has been discussed before.

**How Do I Submit a (Good) Enhancement Suggestion?**
Enhancement suggestions are also tracked as [GitHub issues](https://github.com/sahithuppala05/LogNinja-Keylogger/issues). Create an issue and provide the following information:

*   **Use a clear and descriptive title** for the issue to identify the suggestion.
*   **Provide a detailed description of the proposed enhancement.**
*   **Explain why this enhancement would be useful** to most LogNinja users.
*   **Include screenshots or mock-ups** if applicable.

### Your First Code Contribution

Unsure where to begin contributing? You can start by looking through the `good first issue` and `help wanted` issues. These are typically well-scoped and easier for newcomers.

*   [Good first issues](https://github.com/sahithuppala05/LogNinja-Keylogger/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) - issues which should only require a few lines of code, and a test or two.
*   [Help wanted issues](https://github.com/sahithuppala05/LogNinja-Keylogger/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22) - issues which are a bit more involved than `good first issue` issues.

### Pull Requests

The process described here has several steps, but don't feel you need to complete them all in one go.

1.  **Fork the repository** and create your branch from `main`.
2.  **Set up the development environment** (see below).
3.  **Make your changes.**
4.  **Test your changes thoroughly.**
5.  **Commit your changes** using a descriptive commit message.
    ```bash
    git commit -m "feat: add clipboard monitoring functionality"
    ```
6.  **Push to your fork** and [submit a pull request](https://github.com/sahithuppala05/LogNinja-Keylogger/compare) to the `main` branch.
7.  **Ensure all CI status checks are passing.** (If applicable)
8.  **Respond to any review feedback.**

## Development Setup

To get started contributing code, you need to set up your local environment.

### Prerequisites
*   Python 3.8 or higher
*   Git
*   pip (Python package manager)

### Installation Steps

1.  **Fork and Clone the repo**
    ```bash
    git clone https://github.com/YOUR_USERNAME/LogNinja-Keylogger.git
    cd LogNinja-Keylogger
    ```

2.  **(Recommended) Create a virtual environment**
    ```bash
    python -m venv venv
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    # If you don't have a requirements.txt yet, install manually:
    pip install pynput tkinter
    ```

4.  **Run the application to test your setup**
    ```bash
    python keylogger.py
    ```

## Styleguides

### Git Commit Messages
*   Use the present tense ("Add feature" not "Added feature").
*   Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
*   Consider using the [Conventional Commits](https://www.conventionalcommits.org/) specification.
    *   `feat:` for new features
    *   `fix:` for bug fixes
    *   `docs:` for documentation changes
    *   `style:` for formatting changes
    *   `refactor:` for code refactoring
    *   `test:` for adding tests

### Python Styleguide
*   Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines.
*   Use descriptive variable and function names.
*   Include comments for complex logic.

## Recognition

Your contribution will be recognized in the following ways:
*   Your GitHub profile will be linked in the commit history and pull requests.
*   Significant contributions may earn you a mention in the project's `README.md`.

## Questions?

Feel free to create a new discussion in [GitHub Discussions](https://github.com/sahithuppala05/LogNinja-Keylogger/discussions) if you have any questions or need help getting started.

Happy Coding!
