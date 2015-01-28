c = MongoClient()['db']['collection']

# How many tasks are being queued?
n_docs = c.find(selector).count()

# How many are currently being processed?
process_selector = dict(selector).update({"task.started": True,
                                          "task.completed": False})
n_processing = c.find(process_selector).count()

# How many tasks are completed?
completed_selector = dict(selector).update({"task.completed": True})
n_completed = c.find(completed_selector).count()
