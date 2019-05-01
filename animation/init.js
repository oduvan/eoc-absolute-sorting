//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            functions: {
                js: 'absoluteSorting',
                python: 'absolute_sorting'
            }
        });
        io.start();
    }
);
