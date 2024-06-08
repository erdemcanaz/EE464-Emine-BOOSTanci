

class DataLogger:

    def __init__(self,title:str="Noname", number_of_logs:int=100, inclusive_data_bounds:list[float,float] = None) -> None:
        self.TITLE = title        
        self.NUMBER_OF_LOGS = number_of_logs
        self.INCLUSIVE_DATA_BOUNDS = inclusive_data_bounds
        self.log_array = [0]*number_of_logs

    def append_data(self, new_data: float = 0, should_check_bound:bool=False, raise_if_not_in_bound:bool=False) -> None:
        if should_check_bound:
            if self.INCLUSIVE_DATA_BOUNDS is None:
                raise Exception("Data bounds are not given")
            else:
                is_out_of_boundary = (new_data < self.INCLUSIVE_DATA_BOUNDS[0] or new_data > self.INCLUSIVE_DATA_BOUNDS[1])
                if raise_if_not_in_bound and is_out_of_boundary:
                    raise Exception(" New data is not in given bounds")
                elif is_out_of_boundary:
                    return #do not append this data

        #append new data
        if len(self.log_array) >= self.NUMBER_OF_LOGS:
            self.log_array.pop(0)
        self.log_array.append(new_data)

    def get_title(self):
        return self.TITLE
    
    def get_logs(self):
        return self.log_array
    
    def set_logs(self, data_logs:list[float]=None):
        self.log_array = data_logs
        

