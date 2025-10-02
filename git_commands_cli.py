import subprocess
from git import Repo, GitCommandError

def run_git_command(command):
    result = subprocess.run(["git"] + command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        raise Exception(f"Git command failed: {result.stderr}")
    return result.stdout.strip()

def clone_repository(repo_url, dest_dir):
    return run_git_command(["clone", repo_url, dest_dir])

def show_log(num_lines=5):
    return run_git_command(["log", f"-n{num_lines}"])

def show_summary(n):
    output = run_git_command(["log", f"-n{n}", "--pretty=format:%h - %an, %ar : %s"])
    authors = set()
    for line in output.split("\n"):
        parts = line.split(" : ")
        if len(parts) > 1:
            authors.add(parts[0])
    return authors

def list_branches():
    output = run_git_command(["branch", "-a"])
    branches = [line.strip() for line in output.split("\n")]
    return branches

def commit_changes(repo_path, message):
    try:
        repo = Repo(repo_path)
        repo.git.add(A=True)
        if repo.index.diff("HEAD"):
            repo.index.commit(message)
            return "Changes committed."
        else:
            return "No changes to commit."
    except GitCommandError as e:
        return f"Git command error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"
    
def push_changes(repo_path, remote_name="origin", branch_name="main"):
    try:
        repo = Repo(repo_path)
        origin = repo.remote(name=remote_name)
        origin.push(branch_name)
        return "Changes pushed."
    except GitCommandError as e:
        return f"Git command error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"    