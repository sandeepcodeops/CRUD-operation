from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'flash message'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sandeep'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'uk_police'

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM uk_police.museum")
    data = cur.fetchall()
    cur.close()
    return render_template('index2.html', search_data=data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        objectID = request.form['objectID']
        isHighlight = request.form['isHighlight']
        accessionNumber = request.form['accessionNumber']
        accessionYear = request.form['accessionYear']
        isPublicDomain = request.form['isPublicDomain']
        primaryImage = request.form['primaryImage']
        primaryImageSmall = request.form['primaryImageSmall']
        department = request.form['department']
        objectName = request.form['objectName']
        title = request.form['title']
        culture = request.form['culture']
        artistRole = request.form['artistRole']
        artistPrefix = request.form['artistPrefix']
        artistDisplayName = request.form['artistDisplayName']
        artistDisplayBio = request.form['artistDisplayBio']
        artistAlphaSort = request.form['artistAlphaSort']
        artistNationality = request.form['artistNationality']
        artistBeginDate = request.form['artistBeginDate']
        artistEndDate = request.form['artistEndDate']
        artistWikidata_URL = request.form['artistWikidata_URL']
        artistULAN_URL = request.form['artistULAN_URL']
        objectDate = request.form['objectDate']
        objectBeginDate = request.form['objectBeginDate']
        objectEndDate = request.form['objectEndDate']
        medium = request.form['medium']
        dimensions = request.form['dimensions']
        creditLine = request.form['creditLine']
        geographyType = request.form['geographyType']
        city = request.form['city']
        state = request.form['state']
        county = request.form['county']
        country = request.form['country']
        metadataDate = request.form['metadataDate']
        repository = request.form['repository']
        objectURL = request.form['objectURL']
        objectWikidata_URL = request.form['objectWikidata_URL']
        isTimelineWork = request.form['isTimelineWork']
        GalleryNumber = request.form['GalleryNumber']
        constituents_constituentID = request.form['constituents_constituentID']
        constituents_role = request.form['constituents_role']
        constituents_name = request.form['constituents_name']
        constituents_constituentULAN_URL = request.form['constituents_constituentULAN_URL']
        constituents_constituentWikidata_URL = request.form['constituents_constituentWikidata_URL']
        measurements_elementName = request.form['measurements_elementName']
        measurements_elementDescription = request.form['measurements_elementDescription']
        elementMeasurements_Diameter = request.form['elementMeasurements_Diameter']
        tags_term = request.form['tags_term']
        tags_AAT_URL = request.form['tags_AAT_URL']
        tags_Wikidata_URL = request.form['tags_Wikidata_URL']
        elementMeasurements_Depth = request.form['elementMeasurements_Depth']
        elementMeasurements_Height = request.form['elementMeasurements_Height']
        measurements_elementMeasurements_Width = request.form['measurements_elementMeasurements_Width']
        measurements_elementMeasurements_Weight = request.form['measurements_elementMeasurements_Weight']
        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO museum (objectID,isHighlight,accessionNumber,accessionYear,\
                        isPublicDomain,primaryImage,primaryImageSmall,department,\
                        objectName,title,culture,artistRole,artistPrefix,\
                        artistDisplayName,artistDisplayBio,artistAlphaSort,\
                        artistNationality,artistBeginDate,artistEndDate,\
                        artistWikidata_URL,artistULAN_URL,objectDate,objectBeginDate,\
                        objectEndDate,medium,dimensions,creditLine,geographyType,\
                        city,state,county,country,metadataDate,repository,\
                        objectURL,objectWikidata_URL,isTimelineWork,GalleryNumber,\
                        constituents_constituentID,constituents_role,constituents_name,\
                        constituents_constituentULAN_URL,\
                        constituents_constituentWikidata_URL,measurements_elementName,\
                        measurements_elementDescription,elementMeasurements_Diameter,\
                        tags_term,tags_AAT_URL,tags_Wikidata_URL,\
                        elementMeasurements_Depth,elementMeasurements_Height,\
                        measurements_elementMeasurements_Width,\
                        measurements_elementMeasurements_Weight) VALUES \
                        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (objectID, isHighlight, accessionNumber, accessionYear,
                         isPublicDomain, primaryImage, primaryImageSmall, department,
                         objectName, title, culture, artistRole, artistPrefix,
                         artistDisplayName, artistDisplayBio, artistAlphaSort,
                         artistNationality, artistBeginDate, artistEndDate,
                         artistWikidata_URL, artistULAN_URL, objectDate, objectBeginDate,
                         objectEndDate, medium, dimensions, creditLine, geographyType,
                         city, state, county, country, metadataDate, repository,
                         objectURL, objectWikidata_URL, isTimelineWork, GalleryNumber,
                         constituents_constituentID, constituents_role, constituents_name,
                         constituents_constituentULAN_URL,
                         constituents_constituentWikidata_URL, measurements_elementName,
                         measurements_elementDescription, elementMeasurements_Diameter,
                         tags_term, tags_AAT_URL, tags_Wikidata_URL,
                         elementMeasurements_Depth, elementMeasurements_Height,
                         measurements_elementMeasurements_Width,
                         measurements_elementMeasurements_Weight))

            mysql.connection.commit()
            flash("Data Inserted Successfully")
            return redirect(url_for('index'))
        except Exception:
            flash('Enter a unique values')
            return redirect(url_for('index'))


@app.route('/delete/<string:id_data>', methods=['GET', 'POST'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM museum WHERE objectID=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        objectID = request.form['objectID']
        isHighlight = request.form['isHighlight']
        accessionNumber = request.form['accessionNumber']
        accessionYear = request.form['accessionYear']
        isPublicDomain = request.form['isPublicDomain']
        primaryImage = request.form['primaryImage']
        primaryImageSmall = request.form['primaryImageSmall']
        department = request.form['department']
        objectName = request.form['objectName']
        title = request.form['title']
        culture = request.form['culture']
        artistRole = request.form['artistRole']
        artistPrefix = request.form['artistPrefix']
        artistDisplayName = request.form['artistDisplayName']
        artistDisplayBio = request.form['artistDisplayBio']
        artistAlphaSort = request.form['artistAlphaSort']
        artistNationality = request.form['artistNationality']
        artistBeginDate = request.form['artistBeginDate']
        artistEndDate = request.form['artistEndDate']
        artistWikidata_URL = request.form['artistWikidata_URL']
        artistULAN_URL = request.form['artistULAN_URL']
        objectDate = request.form['objectDate']
        objectBeginDate = request.form['objectBeginDate']
        objectEndDate = request.form['objectEndDate']
        medium = request.form['medium']
        dimensions = request.form['dimensions']
        creditLine = request.form['creditLine']
        geographyType = request.form['geographyType']
        city = request.form['city']
        state = request.form['state']
        county = request.form['county']
        country = request.form['country']
        metadataDate = request.form['metadataDate']
        repository = request.form['repository']
        objectURL = request.form['objectURL']
        objectWikidata_URL = request.form['objectWikidata_URL']
        isTimelineWork = request.form['isTimelineWork']
        GalleryNumber = request.form['GalleryNumber']
        constituents_constituentID = request.form['constituents_constituentID']
        constituents_role = request.form['constituents_role']
        constituents_name = request.form['constituents_name']
        constituents_constituentULAN_URL = request.form['constituents_constituentULAN_URL']
        constituents_constituentWikidata_URL = request.form['constituents_constituentWikidata_URL']
        measurements_elementName = request.form['measurements_elementName']
        measurements_elementDescription = request.form['measurements_elementDescription']
        elementMeasurements_Diameter = request.form['elementMeasurements_Diameter']
        tags_term = request.form['tags_term']
        tags_AAT_URL = request.form['tags_AAT_URL']
        tags_Wikidata_URL = request.form['tags_Wikidata_URL']
        elementMeasurements_Depth = request.form['elementMeasurements_Depth']
        elementMeasurements_Height = request.form['elementMeasurements_Height']
        measurements_elementMeasurements_Width = request.form['measurements_elementMeasurements_Width']
        measurements_elementMeasurements_Weight = request.form['measurements_elementMeasurements_Weight']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE search_data
               SET 
        isHighlight = %s
        accessionNumber =%s
        accessionYear =%s
        isPublicDomain =%s
        primaryImage =%s
        primaryImageSmall =%s
        department =%s
        objectName =%s
        title =%s
        culture =%s
        artistRole =%s
        artistPrefix =%s
        artistDisplayName =%s
        artistDisplayBio =%s
        artistAlphaSort =%s
        artistNationality =%s
        artistBeginDate =%s
        artistEndDate =%s
        artistWikidata_URL =%s
        artistULAN_URL =%s
        objectDate =%s
        objectBeginDate=%s
        objectEndDate=%s
        medium=%s
        dimensions=%s
        creditLine=%s
        geographyType=%s
        city=%s
        state=%s
        county=%s
        country=%s
        metadataDate=%s
        repository=%s
        objectURL=%s
        objectWikidata_URL=%s
        isTimelineWork=%s
        GalleryNumber=%s
        constituents_constituentID=%s
        constituents_role=%s
        constituents_name=%s
        constituents_constituentULAN_URL=%s
        constituents_constituentWikidata_URL=%s
        measurements_elementName=%s
        measurements_elementDescription=%s
        elementMeasurements_Diameter=%s
        tags_term=%s
        tags_AAT_URL=%s
        tags_Wikidata_URL=%s
        elementMeasurements_Depth=%s
        elementMeasurements_Height=%s
        measurements_elementMeasurements_Width=%s
        measurements_elementMeasurements_Weight=%s 
               WHERE objectID=%s
            """, (objectID, isHighlight, accessionNumber, accessionYear,
                         isPublicDomain, primaryImage, primaryImageSmall, department,
                         objectName, title, culture, artistRole, artistPrefix,
                         artistDisplayName, artistDisplayBio, artistAlphaSort,
                         artistNationality, artistBeginDate, artistEndDate,
                         artistWikidata_URL, artistULAN_URL, objectDate, objectBeginDate,
                         objectEndDate, medium, dimensions, creditLine, geographyType,
                         city, state, county, country, metadataDate, repository,
                         objectURL, objectWikidata_URL, isTimelineWork, GalleryNumber,
                         constituents_constituentID, constituents_role, constituents_name,
                         constituents_constituentULAN_URL,
                         constituents_constituentWikidata_URL, measurements_elementName,
                         measurements_elementDescription, elementMeasurements_Diameter,
                         tags_term, tags_AAT_URL, tags_Wikidata_URL,
                         elementMeasurements_Depth, elementMeasurements_Height,
                         measurements_elementMeasurements_Width,
                         measurements_elementMeasurements_Weight))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
