from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import util
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['GET', 'POST'])
def classify():
    if(request.method == "POST"):
        image_data = request.files["file"]
        #save the image to upload
        basepath = os.path.dirname(__file__)
        image_path = os.path.join(basepath, "uploads", secure_filename(image_data.filename))
        image_data.save(image_path)

        predicted_value = util.classify_waste(image_path)
        return redirect(url_for('result',material=predicted_value))

    return render_template('classify.html')

@app.route('/result/<material>')
def result(material):
    
    if material == 'Plastic':
        data = {
            'material': 'Plastic',
            'image': 'plastic',
            'about': 'Plastic is one of the most popular and useful materials of modern times: we now use about 20 times more plastic than we did 50 years ago. Its popularity and widespread use is why handling it responsibly and correctly once it becomes waste is so vitally important. We can optimise the lifespan of plastics by reusing and recycling items as many times as possible. Recycling is a two-stage process: Sorting is mainly done automatically with a manual sort to ensure all contaminants have been removed. Once sorted and cleaned, plastic can either be shredded into flakes or melt processed to form pellets before finally being moulded into new products. There is a wide range of products made from recycled plastic including: refuse sacks and carrier bags, underground drainage systems for homes and national infrastructure, flower pots, seed trays, watering cans and water butts, wheel arch liners and bumpers on cars, damp proof membranes, guttering and window profiles used in construction, reusable crates and pallets, wheel bins and food caddies, composters and wormeries etc.',
            
        }
    elif material == 'Glass':
        data = {
            'material': 'Glass',
            'image': 'glass',
            'about': 'Glass is a very important inorganic material which is one of the largest productions of industries. It can be made into a variety of different products used for man’s daily living. It is an amorphous solid which can have different compositions of semiconductors but most importantly are made of molten silica along with limestone and soda ash. Glass recycling is the process of making glass materials into new glass products. This way, used glass materials pass through a recycling process that requires breaking and melting the glass. To be recycled, glass waste needs to be purified and cleaned of contamination. Then, depending on the end use and local processing capabilities, it might also have to be separated into different colors. Many recyclers collect different colors of glass separately since glass retains its color after recycling.',
            
        }
    elif material == 'Paper':
        data = {
            'material': 'Paper',
            'image': 'paper',
            'about': 'Paper recycling pertains to the processes of reprocessing waste paper for reuse. Waste papers are either obtained from paper mill paper scraps, discarded paper materials, and waste paper material discarded after consumer use. Examples of the commonly known papers recycled are old newspapers and magazines. Other forms like corrugated, wrapping, and packaging papers among other types of paper are usually checked for recycling suitability before the process. The papers are collected from the waste locations then sent to paper recycling facilities. Typically, if one does not recycle, those papers would merely pile up. Worse, they’ll fill up the garbage around and can constitute a nuisance to you and your environment. For instance, it emits toxic gases such as methane and carbon dioxide, which reduces the quality of air.',
            
        }
    elif material == 'Metal':
        data = {
            'material': 'Metal',
            'image': 'metal',
            'about': 'Metals are essential, versatile and can be used in a number of ways. Metals can be used for industrial purposes such as the manufacture of trucks, cars, airplanes, ships, and railways. They can also be used to manufacture domestic items such as cutlery, crockery and even in packaging. The good thing about metal recycling is that metal can be recycled over and over without altering its properties. The most common recyclable metals include aluminum and steel. The other metals, for example, silver, copper, brass and gold, are so valuable that they are rarely thrown away to be collected for recycling. Therefore, they do not create a waste disposal crisis or problem. The metal recycling process is similar to the usual recycling process. The metals are first sorted on the basis of their properties. Metals are resources that are limited. The depletion of metals can be a big issue in the future since the world population grows rapidly and thus also the demand for goods made out of metal will increase.',
            
        }
    elif material == 'Light Bulbs':
        data = {
            'material': 'Light Bulbs',
            'image': 'lightbulbs',
            'about': 'Standard light bulbs should be disposed of in normal household waste. They cannot be recycled as with regular glass, as the fine wires in glass processing are very difficult to separate out and the cost to recycle these items is prohibitive. Compact fluorescent lamps contain small amounts of mercury. Although this is completely safe for users of the lamps, they must be collected separately for disposal. This ensures that valuable parts of the lamps, such as glass and metal, are not lost. Light bulbs often break when thrown into a dumpster, trash can or compactor, or when they end up in a landfill or incinerator. This causes the release of hazardous materials into the environment and can create serious public and environmental health concerns. It’s also important to remember that recycling allows the reuse of the glass, metals and other materials that make up light bulbs. Virtually all components of light bulbs can be recycled.',
            
        }
    elif material == 'Organic':
        data = {
            'material': 'Organic',
            'image': 'organic',
            'about': 'Organic wastes are materials originating from living sources like plants, animals, and microorganisms that are biodegradable and can be broken down into simpler organic molecules. Because of recent shortages in landfill capacity, the number of municipal composting sites for yard wastes is increasing across the country, as is the number of citizens who compost yard wastes in their backyards. On a more limited basis, some mixed municipal waste composting is also taking place. In these systems, attempts to remove inorganic materials are made prior to composting.Food waste from restaurants and grocery stores is typically disposed of through garbage disposals, therefore, it becomes a component of wastewater and sewage sludge. Organic waste recycling is the process of organic waste management where organic wastes are recycled or converted into useful matter by different recycling methods. There are different methods of organic waste recycling, each of which can be used for a particular group of waste to produce some form of useful organic matter. Some of the common methods are Animal feed, Composting, Anaerobic digestion, Rendering etc. ',
        }
    elif material == 'Batteries':
        data = {
            'material': 'Batteries',
            'image': 'batteries',
            'about': 'Battery recycling is the reuse and reprocessing practice of batteries aimed at reducing the number of batteries being disposed of as material waste. Batteries contain several poisonous chemicals and heavy metals and their dumping has attracted environmental concerns due to contamination of water and soil. As such, batteries need recycling to comply with environmental and health benefits. Rechargeable nickel–cadmium (Ni-Cd), nickel metal hydride (Ni-MH), lithium-ion (Li-ion) and nickel–zinc (Ni-Zn), can also be recycled.',
        }
    elif material == 'Clothes':
        data = {
            'material': 'Clothes',
            'image': 'clothes',
            'about': 'Textile recycling is the process by which old clothing and other textiles are recovered for reuse or material recovery. As such, textile recycling is a significant challenge to be addressed as we strive to move closer to a zero landfill society.Once in landfills, natural fibers can take a few weeks to a few years to decompose. They may release methane and CO2 gas into the atmosphere. Additionally, synthetic textiles are designed not to decompose. In the landfill, they may release toxic substances into groundwater and surrounding soil. Textile waste products are gathered from different sources and are then sorted and processed depending on their condition, composition, and resale value. ',
        }
    elif material == 'E-waste':
        data = {
            'material': 'E-Waste',
            'image': 'ewaste',
            'about': 'E-waste is short for electronic waste. That is, trash generated from broken, obsolete, and surplus electronic devices.Typically, these electronics often contain toxic chemicals and hazardous materials. And when not disposed of properly, it can cause the release of toxic substances into our environment. E-waste recycling then refers to the reprocessing and re-use of these electronic wastes. It is simple.  It is a process that seeks to recover material from electronic waste. This way, you can use them in new electronic products. These electronic wastes may be in the form of home appliances like your air conditioners, televisions, electric cookers, air conditioners, heater, DVDs, fans, microwaves, and radios. They may also be in the form of information tech equipment like your computers, laptops, mobile phones, batteries, hard disks, circuit boards, monitors.',
        }
    else:
        data = {
            'material': 'undefined',
            'image':'undefined',
            'about': 'UNDEFINED',
        }

    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)