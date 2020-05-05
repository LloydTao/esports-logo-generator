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


if __name__ == "__main__":

    # Get inputs.
    string = input('Logo text: ')
    stops = []
    colours = int(input('Number of gradient colours: '))
    for i in range(colours):
        offset = "{:.0%}".format(i / (colours - 1))
        colour = input('Gradient colour: ')
        stops.append({"offset": offset,"color": colour})
    graphic = input('Graphic file: ')
    name = input('Logo name: ')

    # Define styles.
    text_styles = ''.join(
        [
            'font-size:128px;',
            'font-family: Rammetto One, Arial;',
            'font-weight:800;',
            'text-transform: uppercase;',
            
            'stroke:black;',
            'stroke-width:8;'
            
            'background: linear-gradient(to right, #30CFD0 0%, #330867 100%);',
            '-webkit-background-clip: text;',
            '-webkit-text-fill-color: transparent;',
        ]
    )
    
    # Create logo.
    logo = create_canvas()
    logo.defs.add(gradient(stops))
    logo = add_text(logo, string, text_styles)
    logo = add_graphic(logo, "graphics/dogs/" + graphic)
    export_canvas(logo, name + ".svg")
