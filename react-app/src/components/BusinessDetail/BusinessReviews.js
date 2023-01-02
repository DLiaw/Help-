import React from "react";

const BusinessReviews = ({ review }) => {
    console.log(review, "######################")
    return (
        <div>
            <h3>Review Highlights</h3>
            <i class="fa-solid fa-user-check" />
            <div>{review.review}</div>
        </div>
    )
}

export default BusinessReviews;
