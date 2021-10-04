def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    items_set = set(items)
    inventory = {}
    for item in items_set:
        inventory[item] = items.count(item)
    return inventory


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    if len(inventory) != 0:
        for item in items:
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1
        return inventory
    return create_inventory(items)


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """
    for item in items:
        if item in inventory and inventory[item] != 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    """

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    list_ = list(tuple(inventory.items()))
    for item in list_[:]:
        if item[1] == 0:
            list_.remove(item)
    return list_
