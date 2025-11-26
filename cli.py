import click
import savef
import branch
import os
@click.group()
@click.option("--ignore-unique", is_flag=True, help="Ignore uniqueness check (For versioning)")
def cli(ignore_unique):
    pass
@cli.command()
def version():
    """Show the version of Mercury."""
    print("Mercury VCS 1.0.1")
    print("Mercury Official CLI Tool")
    print("Any bugs? We'd appreciate a bug report on 'https://github.com/eotter-beep/mercury-vcs/issues'!")
    print("Use --help to get help information")
@cli.command()
@click.argument('file')
def commit(file):
    """Save a file (or files) to Mercury"""
    savef.savefile(file)
@cli.command()
@click.argument('file')
def restart(file):
    """Restart a Mercury branch"""
    branch.restartbranch(file)  # pass the argument
@cli.command()
@click.argument('msg')
def commit_msg(msg):
    """New commit message, If using spaces, enclose them with ""."""
    branch.msg(message=f"{msg}")
@cli.command()
@click.argument('vers')
@click.option("--ignore-unique", is_flag=True, help="Ignore uniqueness check (For versioning)")
def new_ver(vers, ignore_unique):
    """Create a new Mercury version."""
    
    # Check uniqueness unless ignore_unique is True
    if not ignore_unique and os.path.exists(".mrcver"):
        with open(".mrcver", "r") as f:
            current_versions = [line.strip() for line in f.readlines()]
            if vers in current_versions:
                print(f"Error: Version '{vers}' already exists.")
                return  # Stop execution

    print(f"Create version {vers}...")
    os.system("touch .mrcver")
    os.system(f"echo '{vers}' >> .mrcver")

@cli.command()
def list_ver():
    """List all repository versions."""
    branch.readversions()
@cli.command()
@click.argument('msg')
def newrule(msg):
    """Create a commitrules.txt file."""
    branch.commitrules(message=f"{msg}")

if __name__ == '__main__':
    cli(obj={})
