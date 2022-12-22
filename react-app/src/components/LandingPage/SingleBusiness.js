import { NavLink } from "react-router-dom";

const SingleReview = ({ review }) => {
    return (
        <div>
            {/* {review.first_name}{review.last_name} */}
            {/* {<NavLink>{review.business.name}</NavLink>} */}
            {/* {<img alt={'review.id'}>review.review_images[0]</img>} */}
            {review.review}
        </div>
    )
}




export default SingleReview;
