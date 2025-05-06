$(document).on('click', '.print-btn', function() {
    // Wait for the print button click event to trigger the BS conversion
    setTimeout(function() {
        // Loop through the fields in the document and convert any date fields
        $('span[data-fieldname="transaction_date"], span[data-fieldname="posting_date"], span[data-fieldname="due_date"], span[data-fieldname="start_date"], span[data-fieldname="end_date"]').each(function() {
            var ad_date = $(this).text();  // Get the displayed AD date
            if (ad_date) {
                var bs_date = NepaliFunctions.AD2BS(ad_date, "YYYY-MM-DD", "YYYY-MM-DD"); // Convert AD to BS
                $(this).text(bs_date); // Replace AD with BS date in the print preview
            }
        });
    }, 500); // Give some time for the print preview to load
});
