from string import Template

def start_response ( resp = "text/html" ):
    return ( 'Content-type: ' + resp + '\n\n' )

def include_header ( the_title ):
    with open ( 'templates/header.html' ) as headf:
        head_text = headf.read()
    header = Template( head_text )
    return ( header.substitute ( title = the_title ))

def include_footer ( the_links ):
    with open ( 'templates/footer.html' ) as footf:
        foot_text = footf.read ( )
    footer = Template ( foot_text )
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links [ key ] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;'
    return ( footer.substitute ( links = link_string ) )

def output_alist ( the_urls , the_strings ):
    link_string = '<ul>'
    i = 0 
    for each_url in the_urls:
        str1 = the_strings [ i ] 
        i += 1 
        link_string += '<li><a  href="' + each_url + '">' + each_url + '</a></li>' + str1 + '</br></br>'
    link_string += '</ul>'
    return ( link_string )

