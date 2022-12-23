import { NavLink } from "react-router-dom";

const SingleReview = ({ review }) => {
    return (
        <div className="singleReviewCard">
            <div>
                {review.user.first_name}&nbsp;&nbsp;{review.user.last_name.slice(0, 1).toUpperCase()}. <p>Wrote a review</p>
            </div>
            <div className="one">
                <img className="singleReviewCardImg" alt="review-image" src={review.images[0]?.review_image}></img>
            </div>
            <div>
                <NavLink to={`/businesses/${review.business.id}`}>{review.business.name}</NavLink>
            </div>
            <div>
                stars go here
            </div>
            <div>
                {review.review}
            </div>
            <div>
                <NavLink to={`/businesses/${review.business.id}`} >Continue Reading...</NavLink>
            </div>
        </div>
    )
}




export default SingleReview;
