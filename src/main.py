import svgwrite


# Create canvas for logo.
def create_canvas():

    logo = svgwrite.Drawing()
    return logo


# Definine gradient.
def gradient(stops):

    gradient = svgwrite.gradients.LinearGradient(start=(0, 0), end=(0,1), id="gradient")
    for stop in stops:
        gradient.add_stop_color(offset=stop['offset'], color=stop['color'], opacity=None)
    return gradient
    

# Add text to logo.
def add_text(logo, string, styles):

    text = logo.g(style = styles)
    text.add(logo.text(string, insert=(40,120), fill="url(#gradient)"))
    logo.add(text)
    return logo


# Add graphic to logo.
def add_graphic(logo, filename):

    logo.add(logo.image(filename, insert=(40,120)))
    return logo


# Export logo.
def export_canvas(logo, filename):

    try:
        logo.saveas(filename, pretty=True, indent=2)
        print("Saved file to disk!")
    except IOError:
        print("Unable to create file on disk.")
