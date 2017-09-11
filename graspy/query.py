import ast

import inflection

def parse_query(query):
    selectors = [selector.replace("-", "_") for selector in query.split()]
    return [inflection.camelize(selector, uppercase_first_letter=True)
            for selector in selectors]

def search(code, query):
    tree = ast.parse(code)
    selectors = parse_query(query)
    return _search_tree(tree, selectors)

def _search_tree(starting_node, selectors):
    results = []
    selector = selectors[0]
    for node in ast.walk(starting_node):
        # TODO: query needs to be translated
        if isinstance(node, getattr(ast, selector)):
            results.append(node)
    return results
