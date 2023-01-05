import { NavLink } from "react-router-dom";
import './landingPage.css'
import Stars from "../stars";
const SingleReview = ({ review }) => {
    const rating = review.stars
    return (
        <div className="singleReviewCard">
            <div>
                <div className="user-icon-name">
                    <div style={{ height: '5px', color: 'grey' }}>
                        <i class="fa-solid fa-user-pen" />&nbsp;&nbsp;{review.user.first_name}&nbsp;&nbsp;{review.user.last_name.slice(0, 1).toUpperCase()}.
                    </div>
                    <div>
                        <p style={{ height: '5px', color: 'grey' }}>Wrote a review</p>
                    </div>
                </div>
            </div>
            <div className="one">
                <img className="singleReviewCardImg" alt="review-logo" src={review.images[0]?.review_image}></img>
            </div>
            <div className="business-name">
                <NavLink className="business-nav" to={`/business/${review.business.id}`}>{review.business.name}</NavLink>
            </div>
            <div style={{ width: '100px' }}>
                <Stars key={review?.id} rating={rating} />
            </div>
            <div className="review-div">
                {review.review}
            </div>
            <div>
                <NavLink style={{ height: '5px', color: 'grey', textDecoration: 'none' }} to={`/business/${review.business.id}`} >Continue Reading...</NavLink>
            </div>
        </div>
    )
}




export default SingleReview;
