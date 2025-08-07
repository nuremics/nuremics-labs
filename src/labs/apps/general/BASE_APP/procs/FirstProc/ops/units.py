from typing import Optional


def operation(
    param: float,
    outfile: str,
    content: Optional[str] = None,
) -> bool:
    """
    Short description of the function (what it does, in one line).

    Optionally, add a more detailed explanation here. This can include context,
    intended use, assumptions, or side effects.

    Parameters
    ----------
    param : float
        Description of the parameter.
    outfile : str
        Description of the parameter.
    content : str, optional
        Description of the parameter.

    Returns
    -------
    bool
        Description of the returned value.
    """

    # Print operation
    print("<FirstProc operation>")

    # Print input parameters
    print(f"Input Parameter: {param}")

    # Print input paths
    content_exist = False
    if content is not None:
        content_exist = True
        print(f"Input Path: {content}")

    # Write outputs
    with open(outfile, "w") as file:
        file.write('[FirstProc] file created defined by "outfile".')
    
    # Return internal outputs
    return content_exist