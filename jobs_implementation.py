from collections import deque

def job_a():
    print("Executing Job A")

def job_b():
    print("Executing Job B")

def job_c():
    print("Executing Job C")

def job_d():
    print("Executing Job D")

def job_e():
    print("Executing Job E")

graph = {
    "job_a": ["job_b", "job_c"],
    "job_b": [],
    "job_c": ["job_d"],
    "job_d": [],
    "job_e": ["job_d"]
}

def get_in_degree(graph):
    in_deg = {job: 0 for job in graph}
    for deps in graph.values():
        for dep in deps:
            in_deg[dep] += 1
    return in_deg

def execute_jobs(graph):
    in_degree = get_in_degree(graph)

    queue = deque([job for job in in_degree if in_degree[job] == 0])
    executed_jobs = []

    while queue:
        current_job = queue.popleft()
        func = globals()[current_job]
        func()
        executed_jobs.append(current_job)

        for dependent in graph[current_job]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    if len(executed_jobs) != len(graph):
        print("Cycle detected or some jobs could not be executed.")
    else:
        print("All jobs executed successfully.")