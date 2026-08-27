<div align="center">
  <img src="./banner.jpg" alt="Fast" width=100%>
</div>

# Fast

Fast is a file generator designed to help you build applications faster.

The principle is simple: you have templates, and whenever you want to add a page, a component, a library, or basically anything to your project (even the foundation of the project itself), Fast will generate the files.

Fast works with a variable system. For example, if some files in your template contain `{{lower_name}}`, Fast will replace all occurrences with the name of the element you are currently adding. This allows each file to be modified on the fly as it is being added.

# Prerequisites

| All systems             | Windows           | Linux and MacOS  |
| ----------------------- | ----------------- | ---------------- |
| `Python 3.14 (minimum)` | `PowerShell`      | `cURL and Unzip` |

## Command installation

You just need to enter a single command to install Fast:

* Windows (PowerShell) : `iex (irm https://github.com/TheRake66/python-fast/raw/refs/heads/main/install.ps1)`
* Linux / MacOS : `curl -sSL https://github.com/TheRake66/python-fast/raw/refs/heads/main/install.sh | bash`

## Installation folder

| Windows         | Linux            | MacOS                                |
| --------------- | ---------------- | ------------------------------------ |
| `%appdata\Fast` | `~/.config/Fast` | `~/Library/Application Support/Fast` |

## Folder structure

* `Fast` : Installation folder.
  * `modules` : The folder containing your custom variable modules.
  * `settings` : The folder containing your custom settings.
  * `templates` : The folder containing your custom templates.

The other folders contain Fast source code, so you do not need to access them.

## CLI Arguments

* `fast` : Main command.
  * `create` : Create a new element to your project from a template.
    * `key` : Template key in the settings file.
    * `name` : Name of the element to add.
    * `?extras` : Additional constants to add to the process.
  * `delete` : Delete an existing element in your project from a template.
    * `key` : Template key in the settings file.
    * `name` : Name of the element to delete.
    * `?extras` : Additional constants to add to the process.
  * `start` : Start a service in the system terminal.
    * `key` : Service key in the settings file.
  * `load` : Load another settings file.
    * `name` : Filename of settings without suffix.
  * `check` : Check intergity of an existing element from a template.
    * `key` : Template key in the settings file.
    * `name` : Name of the element to check.
    * `?extras` : Additional constants to add to the process.
  * `pack` : Pack current folder into a template.
    * `?name` : Name of the output archive for template.
  * `infos` : Display many informations about current settings.
  * `root` : Open installation folder in file explorer.
  * `open` : Open current folder in file explorer.
  * `git` : Open source code repository in web browser.

Parameters with `?` are optional.

## Predefined variables

Fast includes variables built on the fly using the name of the element you are currently adding.

Here is an example for the name `package-subpackage-name` :

| Variable                    | Result                    |
| --------------------------- | ------------------------- |
| `{{lower_name}}`            | `name`                    |
| `{{upper_name}}`            | `NAME`                    |
| `{{title_name}}`            | `Name`                    |
| `{{relative_dir}}`          | `../../`                  |
| `{{relative_parent}}`       | `../../../`               |
| `{{relative_path_lower}}`   | `../../name`              |
| `{{relative_path_upper}}`   | `../../NAME`              |
| `{{relative_path_title}}`   | `../../Name`              |
| `{{namespace_ossep_lower}}` | `package\subpackage\name` |
| `{{namespace_ossep_upper}}` | `PACKAGE\SUBPACKAGE\NAME` |
| `{{namespace_ossep_title}}` | `Package\Subpackage\Name` |
| `{{namespace_slash_lower}}` | `package\subpackage\name` |
| `{{namespace_slash_upper}}` | `PACKAGE\SUBPACKAGE\NAME` |
| `{{namespace_slash_title}}` | `Package\Subpackage\Name` |
| `{{namespace_back_lower}}`  | `package/subpackage/name` |
| `{{namespace_back_upper}}`  | `PACKAGE/SUBPACKAGE/NAME` |
| `{{namespace_back_title}}`  | `Package/Subpackage/Name` |
| `{{namespace_dash_lower}}`  | `package-subpackage-name` |
| `{{namespace_dash_upper}}`  | `PACKAGE-SUBPACKAGE-NAME` |
| `{{namespace_dash_title}}`  | `Package-Subpackage-Name` |
| `{{namespace_under_lower}}` | `package_subpackage_name` |
| `{{namespace_under_upper}}` | `PACKAGE_SUBPACKAGE_NAME` |
| `{{namespace_under_title}}` | `Package_Subpackage_Name` |
| `{{namespace_dots_lower}}`  | `package.subpackage.name` |
| `{{namespace_dots_upper}}`  | `PACKAGE.SUBPACKAGE.NAME` |
| `{{namespace_dots_title}}`  | `Package.Subpackage.Name` |

The `ossep` variables match the namespace separator with the file system separator (`\` for Windows, `/` for Linux and macOS). This allows the variable to be included in the file name to create subfolders directly using the package names.

In the same example, a file named `{{namespace_ossep_lower}}.tsx` will result in the following file tree:
```
└─package
    └─subpackage
       └──name.tsx
```

## Add settings

In the Fast installation folder, you will find a `settings` folder containing your settings files for Fast.

The `react-fastapi.json` settings file is included as an example. It allows you to develop a React (with TypeScript) + FastAPI web application.

Create your own settings files based on the last one (for example: `godot.json` with your templates for game development).

## Add variables

### With settings file

In your settings files, you have a `variables` section where you can add your custom constants.

Example: `"creator_name": "TheRake66"`

### With CLI arguments

When executing a command, you can pass an infinite number of custom constants:

Example: `fast add component button --creator_name=TheRake66`

### With modules

Inside the Fast installation folder, there is a `modules` folder. It contains all the scripts that you can load in the `modules` section of your settings files. When executing a command, each script is executed, and a `variables` dictionary placed at the root of the module is retrieved and added to the variables.

Example:
```python
# foo.py
variables: dict[str, str] = {
  "creator_name": "TheRake66"
}
```

## Variables priority

Variables are loaded in a specific order. Variables loaded later will overwrite previous ones:
1. `Predefined variables`
2. `From loaded modules`
3. `From settings file`
4. `From CLI arguments`

## File extensions

Fast does not modify the content of all files, only those whose extension is listed in the `suffixs` array of the settings file.

## Modify templates

To use your own templates, simply put the URLs or paths in the `templates` section of the settings file.

Here is an example for adding a C# library: `"libcs": "https://.../library_csharp.zip"`

You can also put your templates in the `templates` folder inside the Fast installation folder to keep them offline.

In the settings file: `"libcs": "templates/library_csharp.zip"`

## Add service

Fast integrates a command shortcut system called a service. It allows you to quickly run a command. You will find the list of services in the `services` section of the settings file, like this:
`"key": "command"`

Here is an example to open the calculator:
`"calc": "start calc.exe"`