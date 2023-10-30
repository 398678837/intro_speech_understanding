
def list_to_dict(input_list):
    '''
    This function should return a dictionary in which each element of 
    `input_list` is a value, and the corresponding key is the numerical 
    index of that element in `input_list`. 
    '''
    output_list = {}
    index = 0
    
    for items in input_list :
        output_list[index]=items
        index = index +1
        
    return output_list
            
        




