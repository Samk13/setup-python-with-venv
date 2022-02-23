test = {
    "key4": "asdfdsf",
    "key5": {
        "key6": "result2",
        "key7": ["asdf", "asdf"]
    },
    "key8": [{
        "key9": "result3"
    }],
    "key10": [],
    "key11": [
        {
            "key12": "result4",
            "key13": ["result5", "result6"],
        },
        {
            "key14": "result6",
            "key15": "result7",
        }
    ]
}


# def get_response_value(res=None, *keys):
#     result = res
#     try:
#         for k in keys:
#             if isinstance(result, dict) and isinstance(k, str):
#                 result = result.get(k)
#                 if result is None:
#                     return None
#             elif isinstance(k, int) and isinstance(result[k], list) and len(result) > k >= 0:
#                 result = result[k]
#             else:
#                 return None
#     except Exception as e:
#         raise e
#     return result
def get_safe_list_value(res: list, index: int):
    try:
        return res[index]
    except Exception as e:
        raise IndexError(f"Index {index} is out of range")


def get_response_value(res: dict, *keys):
    result = res
    for k in keys:
        if not isinstance(result, dict) and isinstance(k, str):
            result = get_safe_list_value(result, k)
        result = result[k]
        if result is None:
            return None
    return result

# get safe list value


# print(get_response_value(test, "key11", 0, "key12"))
# print(get_response_value(test, "key4"))
# print(get_response_value(test, "key4"))
# print(get_response_value(test, "key5", "key7"))
print(get_response_value(test, "key11", 0, "key13"))
# x = get_response_value(test, "key11")
# print(x)
# print(get_response_value(get_safe_list_value(x, 1), "key12"))
