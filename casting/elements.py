class Elements:
    """A collection of elements.

    The responsibility of a cast is to keep track of a collection of objects. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _elements (dict): A dictionary of objects { key: group_name, value: a list of objects }
    """

    def __init__(self):
        """Constructs a new Object."""
        self._elements = {}
        
    def add_object(self, group, object):
        """Adds an object to the given group.
        
        Args:
            group (string): The name of the group.
            elements (object): The object to add.
        """
        if not group in self._elements.keys():
            self._elements[group] = []
            
        if not object in self._elements[group]:
            self._elements[group].append(object)

    def get_elements(self, group):
        """Gets the elements in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The elements in the group.
        """
        results = []
        if group in self._elements.keys():
            results = self._elements[group].copy()
        return results
    
    def get_all_elements(self):
        """Gets all of the elements in the cast.
        
        Returns:
            List: All of the elements in the cast.
        """
        results = []
        for group in self._elements:
            results.extend(self._elements[group])
        return results

    def get_first_object(self, group):
        """Gets the first element in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first element in the group.
        """
        result = None
        if group in self._elements.keys():
            result = self._elements[group][0]
        return result

    def remove_object(self, group, object):
        """Removes an element from the given group.
        
        Args:
            group (string): The name of the group.
            element (element): The element to remove.
        """
        if group in self._elements:
            self._elements[group].remove(object)