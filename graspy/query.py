import ast


SELECTOR_MAPPING = {
    'class-def': ast.ClassDef
}

def build_type_selector(value):
    return lambda node: isinstance(node, SELECTOR_MAPPING.get(value))

def parse_query(query):
    # TODO: Break these out more
    return [build_type_selector(part) for part in query.split()]

def search(code, query):
    tree = ast.parse(code)
    selectors = parse_query(query)
    return _search_tree(tree, selectors)

def _search_tree(starting_node, selectors):
    results = []
    selector = selectors[0]
    for node in ast.walk(starting_node):
        if selector(node):
            results.append(node)
    return results
