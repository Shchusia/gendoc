"""
commands to build documentation
"""
import click

from gendoc import DocGenerator
from gendoc.settings import AllowedSaveModes
from gendoc.utils.config_handler import copy_config, load_config
from gendoc.utils.utils import get_extensions


@click.group()
def entry_point():
    pass


@entry_point.command("init", help="Setup config file for generating documentation")
@click.option(
    "-f",
    "--file-config",
    "file_config",
    show_default=True,
    required=False,
    default="gen_doc.yaml",
    help="Config file name",
    type=str,
)
@click.option(
    "-o",
    "--overwrite",
    "overwrite",
    is_flag=True,
    required=False,
    default=False,
    help="for overwriting if file exist",
    type=bool,
)
def init(file_config: str, overwrite: bool):
    welcome_string = """Config was created"""
    is_correct = copy_config(file_config, overwrite)
    if not is_correct:
        return
    print(welcome_string)


@entry_point.command("build", help="build documentation")
@click.argument(
    "language",
    required=False,
    default="py",
    type=click.Choice(list(get_extensions().keys())),
)
@click.option(
    "-sm",
    "--save-mode",
    "save_mode",
    required=False,
    default="md",
    help="save mode",
    type=click.Choice([i.name for i in AllowedSaveModes]),
)
@click.option(
    "-hi",
    "--hierarchically",
    "hierarchically",
    is_flag=True,
    required=False,
    default=True,
    help="extract with same hierarchy",
    type=bool,
)
@click.option(
    "-o",
    "--overwrite",
    "overwrite",
    is_flag=True,
    required=False,
    default=True,
    help="for overwriting if file exist",
    type=bool,
)
@click.option(
    "-p2r",
    "--path-to-root",
    "path_to_root",
    required=False,
    default=None,
    help="path to the directory for which documentation should be compiled",
    type=str,
)
@click.option(
    "-p2s",
    "--path-to-save",
    "path_to_save",
    required=False,
    default=None,
    help="path to the directory where to save docs",
    type=str,
)
@click.option(
    "-f2s",
    "--file-to-save",
    "file_to_save",
    required=False,
    default=None,
    help="path to the directory where to save docs",
    type=str,
)
@click.option(
    "-c",
    "--config",
    "config",
    is_flag=True,
    required=False,
    default=False,
    help="Config file name",
    type=bool,
)
@click.option(
    "-f",
    "--file-config",
    "file_config",
    show_default=True,
    required=False,
    default="gen_doc.yaml",
    help="Config file name",
    type=str,
)
def build(
    language,
    save_mode,
    path_to_root,
    config,
    hierarchically,
    overwrite,
    path_to_save,
    file_to_save,
    file_config,
):
    extensions = get_extensions()
    if config:
        configs = load_config(file_config)
        if not config:
            print("Specified incorrect or broken file")
            return
        options = configs.get("OPTIONS", dict())
        author = configs.get("AUTHOR", dict())
        project = configs.get("PROJECT", dict())

        if "language" not in options:
            print(
                "Please don't drop required fields from config. "
                "Add field `language` to config and try again."
            )
            return
        if options["language"] not in extensions:
            print(
                f"You specified an unavailable value for languages. "
                f"Available values {list(extensions.keys())}"
            )

        parser = extensions[options["language"]](
            path_to_root_folder=options.get("path_to_root_folder", None),
            extract_with_same_hierarchy=options.get(
                "extract_with_same_hierarchy", True
            ),
            overwrite_if_file_exists=options.get("overwrite_if_file_exists", False),
            path_to_save=options.get("path_to_save", None),
            file_to_save=options.get("file_to_save", None),
            save_mode=options.get("save_mode", "md"),
            additional_files_to_ignore=options.get("additional_files_to_ignore", None),
            additional_folders_to_ignore=options.get(
                "additional_folders_to_ignore", None
            ),
            title=project.get("title"),
            repository_main_url=project.get("repository"),
            release=project.get("release"),
            author=author.get("author"),
            author_contacts=author.get("author_contacts"),
        )  # type: DocGenerator
    else:
        parser = extensions[language](
            path_to_root_folder=path_to_root,
            extract_with_same_hierarchy=hierarchically,
            overwrite_if_file_exists=overwrite,
            path_to_save=path_to_save,
            file_to_save=file_to_save,
            save_mode=save_mode,
        )
    parser.build_documentation()


if __name__ == "__main__":
    entry_point()
