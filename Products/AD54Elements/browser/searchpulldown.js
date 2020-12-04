jQuery(document).ready(function($) {

    /** FUNCTIONS **/

    function input_searchstring_focus() {
        $('ul#search').addClass('show');
        $('#portal-searchbox').addClass('topborderradius');
        // unbind ourself to avoid looping
        $('input#searchString').off('focus.searchstring');
        // allows the user to arrow through the options
        $('ul#search.show li label input:checked').focus();
    }

    function clear_searchString() {
        // Clear the box if it has the default 'Type To Search' only. Don't want to erase it if there is already a search term
        var searchValue = $('input#searchString').val();
        if (searchValue == 'Type To Search...') {
            $('input#searchString').val('');
        }
    }

    function focus_to_searchbox() {
        $('input#searchString').select();
        clear_searchString();
    }

    function close_searchbox() {
        $('ul#search').removeClass('show');
        $('#portal-searchbox').removeClass('topborderradius');
        if ($(':focus').closest('ul.ad54-search-menu').length) {
            // focus was in the search menu, refocus to the search input
            $('input#searchString').select();
        } else {
            $('ul#search li label input').blur();
        }
        // rebind so the box can re-open
        $('input#searchString').on('focus.searchstring', input_searchstring_focus);
    }

    function click_open_search_options() {
        //$('ul#search').addClass('show');
        $('#portal-searchbox').addClass('topborderradius');
        clear_searchString()
        $('input#searchString').select();
    }



    /** EVENT HANDLERS **/

    /**
     * EVENT: Enter pressed on one of the search menu radio buttons
     */
    $('ul#search li label input').on(
        'keypress',
        function (event) {
            // If 'Enter' is clicked go to the searchbox input
            // and do NOT submit the form
            if (event.keyCode == 13) {
                // Stop the default Enter.
                // IE doesn't understand 'preventDefualt'
                //   but it does understand 'returnValue'
                (event.preventDefault) ? event.preventDefault() : event.returnValue = false;
                focus_to_searchbox();
            }
        }
    );

    /**
     * EVENT: Space Bar pressed on one of the search menu labels
     */
    $('ul#search li label').on(
        'keyup',
        function(event) {
            // If the 'space bar' is pressed, go to the searchbox input
            if (event.keyCode == 32) {
                focus_to_searchbox();
            }
        }
    );

    /**
     * EVENT: ESC pressed anywhere; close the search menu
     */
    $('body').on(
        'keydown',
        function(event) {
            var code = event.keyCode ? event.keyCode : event.which;
            if (code == 27) {
                // ESC key is pressed, close the searchbox
                close_searchbox();
            }
        }
    );

    /**
     * EVENT: search input gets the focus
     *
     * this is the initial binding
     */
    $('input#searchString').on('focus.searchstring', input_searchstring_focus);

    /**
     * EVENT: clicking the search input opens the search menu
     */
    $('input#searchString').on('click', click_open_search_options);

    /**
     * EVENT: Allow clicking anywhere outside the search to close the search menu
     */
    $('div#portal-searchbox').on(
        'click',
        function(event) {
            // keep click events from leaving the searchbox
            // to avoid clicks in the searchbox from triggering the
            // search menu to close
            event.stopPropagation();
        }
    );
    // allow the user to click anywhere and close the search menu
    $('html').on('click', close_searchbox);



    /** INITIALIZATION **/

    // If JavaScript is enabled, disable the CSS functionality
    // Otherwise the CSS options will handle making the search features available
    $('ul#menu').removeClass('show');
});

