def worker_daemon(selector):
    c = MongoClient()['db']['collection']
    sel = {'task': {'$exists': False},
           'task.started': False}
    selector.update(sel)

    claim_doc = lambda: c.find_and_modify(
        query=selector,
        update={'$set': {'task.started': True,
                         'task.completed': False}},
        new=True)

    doc = claim_doc()
    while doc:
        results = process(doc)
        results.update({'task.completed': True})
        c.update({'_id': doc['_id']},
                 {'$set': results})

        doc = claim_doc()
