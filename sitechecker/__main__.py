import sys
import pathlib

from sitechecker.checker import site_is_online
from sitechecker.cli import display_check_result, read_user_cli_args

def main():
    user_args = read_user_cli_args()
    urls = _get_url_list(user_args)

    if not urls:
        print("No URL found")
        sys.exit(1)
    _site_check(urls)


def _get_url_list(user_args):
    """ Append all URLs passed as arguments to
        the url list fetched from file. 
    """
    urls = user_args.urls 
    
    if user_args.input_file:

        urls += _fetch_urls(user_args.input_file)
    return urls

def _fetch_urls(file):
    """ Check file for content, read through lines,
        and return a list off appended urls 
    """
    file_path = pathlib.Path(file)

    if file_path.is_file():
        
        with file_path.open() as fp:
            
            urls = [url.strip() for url in fp]
            
            if urls:
                return urls
            else:
                print(f"Error: file {file} is empty", file=sys.stderr)
    else:
        print("Error: File not found", file=sys.stderr)
        return []

def _site_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

if __name__ == "__main__":
    main()