from typing import Optional


def operation(
    content: str,
    outfile1: str,
    outfile2: str,
    param: Optional[int] = None,
) -> bool:
    """
    Short description of the function (what it does, in one line).

    Optionally, add a more detailed explanation here. This can include context,
    intended use, assumptions, or side effects.

    Parameters
    ----------
    content : str
        Description of the parameter.
    outfile1 : str
        Description of the parameter.
    outfile2 : str
        Description of the parameter.
    param : int, optional
        Description of the parameter.

    Returns
    -------
    bool
        Description of the returned value.
    """

    # Print operation
    print("<SecondProc operation>")

    # Print input parameters
    param_exist = False
    if param is not None:
        param_exist = True
        print(f"Input Parameter: {param}")

    # Print input paths
    print(f"Input Path: {content}")

    # Write outputs
    with open(outfile1, "w") as file:
        file.write('[SecondProc] first file created in folder defined by "outfolder".')
    with open(outfile2, "w") as file:
        file.write('[SecondProc] second file created in folder defined by "outfolder".')
    
    # Return internal outputs
    return param_exist