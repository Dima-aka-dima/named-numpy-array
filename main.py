import numpy as np

def getNamedNumpyClass(className, variableNames):
    
    namedClass = type(className, (np.ndarray,), {
        'dict': dict(zip(variableNames, range(len(variableNames))))})
    
    # creation from np.ndarray
    def _new(self, array):

        assert (len(self.dict), ) == array.shape, f"Shape should be {(len(self.dict), )}"
        return array.view(self)

    # update array on setting variables
    def _setattr(self, name, value):
        if name in self.dict: self[self.dict[name]] = value
        else: self[name] = value
      
    # addressing variables as attributes
    def _getattr(self, name):
        if name in self.dict: name = self.dict[name]
        return self[name]
        
    setattr(namedClass, '__new__', _new)
    setattr(namedClass, '__setattr__', _setattr)
    setattr(namedClass, '__getattr__', _getattr)
        
    return namedClass


def getNamedNumpyArrayClass(className, variableNames):
    
    namedClass = type(className, (np.ndarray,), {
        'dict': dict(zip(variableNames, range(len(variableNames))))})
    
    # creation from np.ndarray
    def _new(self, array):
        assert len(self.dict) == array.shape[-1], f"Last dimension should be {len(self.dict)}."
        return array.view(self)

    # update array on setting variables
    def _setattr(self, name, value):
        if name in self.dict: self[...,self.dict[name]] = value
        else: self[name] = value
      
    # addressing variables as attributes
    def _getattr(self, name):
        if name in self.dict: return self[...,self.dict[name]]
        else: return self[name]
        
    setattr(namedClass, '__new__', _new)
    setattr(namedClass, '__setattr__', _setattr)
    setattr(namedClass, '__getattr__', _getattr)
        
    return namedClass
    
## Another useful variation with automatic type conversion

def getNamedNumpyArrayClassTyped(className, variableNames, dtype = np.float64):
    
    namedClass = type(className, (np.ndarray,), {
        'dict': dict(zip(variableNames, range(len(variableNames))))})
    
    # creation from np.ndarray
    def _new(self, array, dtype = dtype):
        if isinstance(array, list): array = np.array(array, dtype = dtype)
        assert len(self.dict) == array.shape[-1], f"Last dimension should be {len(self.dict)}."
        return array.astype(dtype).view(self)

    # update array on setting variables
    def _setattr(self, name, value):
        if name in self.dict: self[...,self.dict[name]] = value
        else: self[name] = value
      
    # addressing variables as attributes
    def _getattr(self, name):
        if name in self.dict: return self[...,self.dict[name]]
        else: return self[name]
        
    setattr(namedClass, '__new__', _new)
    setattr(namedClass, '__setattr__', _setattr)
    setattr(namedClass, '__getattr__', _getattr)
        
    return namedClass
    
## This is typed version but mypy doesn't like it

# from typing import List, Any
# from numpy.typing import NDArray, DTypeLike

# def getNamedNumpyClass(className: str, variableNames: List[str], T: DTypeLike = np.generic):
#     
#     namedClass = type(className, (np.ndarray,), {
#         'dict': dict(zip(variableNames, range(len(variableNames))))})
#     
#     # creation from np.ndarray
#     def _new(self, array: NDArray[T]):
# 
#         assert (len(self.dict), ) == array.shape, f"Shape should be {(len(self.dict), )}"
#         return array.view(self)
# 
#     # update array on setting variables
#     def _setattr(self, name, value):
#         if name in self.dict: self[self.dict[name]] = value
#         else: self[name] = value
#       
#     # addressing variables as attributes
#     def _getattr(self, name):
#         if name in self.dict: name = self.dict[name]
#         return self[name]
#         
#     setattr(namedClass, '__new__', _new)
#     setattr(namedClass, '__setattr__', _setattr)
#     setattr(namedClass, '__getattr__', _getattr)
#         
#     return namedClass
# 
# 
# def getNamedNumpyArrayClass(className: str, variableNames: List[str], T: DTypeLike = np.generic):
#     
#     namedClass = type(className, (np.ndarray,), {
#         'dict': dict(zip(variableNames, range(len(variableNames))))})
#     
#     # creation from np.ndarray
#     def _new(self, array: NDArray[T]):
#         assert len(self.dict) == array.shape[-1], f"Last dimension should be {len(self.dict)}."
#         return array.view(self)
# 
#     # update array on setting variables
#     def _setattr(self, name, value):
#         if name in self.dict: self[...,self.dict[name]] = value
#         else: self[name] = value
#       
#     # addressing variables as attributes
#     def _getattr(self, name):
#         if name in self.dict: return self[...,self.dict[name]]
#         else: return self[name]
#         
#     setattr(namedClass, '__new__', _new)
#     setattr(namedClass, '__setattr__', _setattr)
#     setattr(namedClass, '__getattr__', _getattr)
#         
#     return namedClass
# 
