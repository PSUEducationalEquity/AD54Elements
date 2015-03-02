Description

    Products.AD54Elements is a Penn State-specific Plone product which provides
    several viewlets and scripts to provide a starting point in complying with
    Penn State Policy AD-54.

    Starting with version 2.0, you must install this product in a Plone
    instance for it to have any effect.  It does not affect other Plone
    instances running on the same Zope server because the viewlets
    are registered to a browser layer that is only available when the
    product is installed.  

    The logo viewlet will automatically insert a unitlogo.png if it
    made available via a skin layer or added as an image object to
    the root of a site.

    The standard searchbox is replaced with a multiple-search box
    that can search Penn State sites, directories, etc.  The items in the
    search box can be configured through portal_properties in the ZMI.
    The searchKeys, searchLinks, and searchDescription fields are linked
    by line number, i.e. the first line of each is merged to create
    a search item.  The searchKeys are the short name (the value in the
    option tags), the searchLinks are the links for the search targets
    with a "%s" to indicate where the search keyword(s) should be inserted,
    and searchDescriptions contain the text displayed in the dropdown
    list.  The searchDefaultKey allows a particular item to be selected
    by default.

    The footer is also adjusted to include required statements.

    NOTE: This product is not a complete theme by itself.
    NOTE: When you download this product you should name it Products.AD54Elements
    
Installation

	In your buildout.cfg file, add Products.AD54Elements to the [eggs] section:

	eggs =
    	Plone
    	Products.AD54Elements

	And add src/Products.AD54Elements to the [develop] section:

	develop =
    	src/Products.AD54Elements

	Run buildout, then start your Plone instance.  AD54Elements will appear
    in the Add/Remove Products configlet (and in the portal_quickinstaller
    in the ZMI) and can be installed and uninstalled.

    On the file system: place AD54Elements in the Products directory
    of your Zope instance and restart the server.  Use the Plone
    Add/Remove Products configlet (or portal_quickinstaller) to install
    AD54Elements.

    To do a complete reinstall and revert to default settings,
    uninstall AD54Elements from the Add/Remove Products configlet (or
    portal_quickinstaller), go to portal_properties in the ZMI and delete
    the ad54elements_properties properties sheet, then install AD54Elements
    again.

Integration with Eggified Theme Products

    Instead of using the above instructions to explictly install AD54Elements,
    you may call it in as a dependency of your theme product.  You only need to
    make a few changes to your product.  This procedure should work with any
    buildout-based Plone 3.2 or later for any egg-style theme product.

    First, edit the setup.py at the top-level
    of your theme product egg and add 'Products.AD54Elements', to the
    install_requires list and
    'https://weblion.psu.edu/svn/weblion/weblion/AD54Elements/dist/' to the
    dependency_links section.  Here are some excerpts of what the changes look
    like (there may be additional code between these sections):

        dependency_links = [
            'https://weblion.psu.edu/svn/weblion/weblion/AD54Elements/dist/',
        ],

        install_requires = [
            'setuptools',
            'Products.AD54Elements',
        ],

    Second, edit the metadata.xml file in your GenericSetup install profile
    (typically your.product/your/product/profiles/default/metadata.xml) to
    include a depenecies section like follows:

        <dependencies>
            <dependency>profile-Products.AD54Elements:default</dependency>
        </dependencies>

    Here is a full example of a metadata.xml file in case your product does
    not already have one:

        <?xml version="1.0"?>
        <metadata>
            <version>1</version>
            <dependencies>
                <dependency>profile-Products.AD54Elements:default</dependency>
            </dependencies>
        </metadata>

    At this point you can re-run buildout and you should see AD54Elements
    downloaded as a dependency.  Then just reinstall your theme product via
    the Plone control panel or portal_quickinstaller and AD54Elements should
    be automatically installed.

Upgrading

    When upgrading from version 1.x you must follow the installation
    instructions above.

    When upgrading from version 2.0, you must run the upgrade step in
    Plone's Add/Remove Products configlet before the search functionality
    will work correctly.  Note: Reinstalling will also work if no
    upgrade button is available in your version of Plone.

    When upgrading from version 2.x, you should check any custom CSS
    for references to the ad54box id, as it has been replaced by the standard
    portal-logo id and the content has been divided into divs for the 
    Penn State mark (psu-icon), the unit (unit-id), and the unit logo
    (unit-logo).  Also be aware that version 3.0 and greater include
    a default favicon and an apple devices icon.

License

    Copyright (c) 2008-11 The Pennsylvania State University. WebLion is
    developed and maintained by the WebLion Project Team, its partners, and
    members of the Penn State Zope Users Group.

    This program is free software; you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the Free
    Software Foundation; either version 2 of the License, or (at your option)
    any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
    more details.

    You should have received a copy of the GNU General Public License along with
    this program; if not, write to the Free Software Foundation, Inc., 59 Temple
    Place, Suite 330, Boston, MA 02111-1307 USA.
