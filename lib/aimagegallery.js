/**
 * Created by adam.
 */

(function ( $ ) {
    $.fn.aimagegallery = function(options){

        options = $.extend(true, {
            option: 'value'
        }, options);

        $(this).each(function(){

          //on mouseenter
          $(this).mouseenter(function() {
            //clone image and hover it over
            clone = $(this).find('.gallery_img').clone().addClass('img_clone');
            $(this).append(clone);

            //make label visible
            $(this).find('.gallery_label').addClass('label_show');

            //animate increasing size on image and lable
            clone.addClass('bigger_img', 200);
            $(this).find('.gallery_label').addClass('bigger_label', 200);

          });

          //on mouseleave
          $(this).on('mouseleave', function() {
            //remove popped-out image
            $(this).find('.img_clone').remove();
            //hide and shrink the label
            $(this).find('.gallery_label').removeClass('label_show');
            $(this).find('.gallery_label').removeClass('bigger_label');
          });

        });

        return this;
    };
}( jQuery ));
