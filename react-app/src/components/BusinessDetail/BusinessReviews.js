import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, useHistory } from "react-router-dom";
import { deleteOldReview } from '../../store/review'
import Stars from '../stars'
const BusinessReviews = ({ singleReview }) => {
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const history = useHistory()

    const handleSubmit = async (e) => {
        e.preventDefault()
        dispatch(deleteOldReview(singleReview.id))
        history.push(`/business/${singleReview.business_id}`)
        history.go(0)
    }
    const rating = singleReview.stars

    if (!rating) return null;
    return (
        <div className="business-details">
            <div className="business-review-div">
                <i style={{ fontSize: '25px' }} class="fa-solid fa-user-check" />
                <div style={{ paddingTop: '9px' }}>{singleReview.user.first_name}&nbsp;&nbsp;{singleReview.user.last_name[0].toUpperCase()}.</div>
            </div>
            <div className="stars-date">
                <div style={{ width: '100px' }}>
                    <Stars key={singleReview?.id} rating={rating} />
                </div>
                &nbsp;&nbsp;
                <div>
                    {new Date(singleReview.created_at).toDateString()}
                </div>
                <div>
                    {user.id == singleReview.user_id && user && <div>
                        &nbsp;&nbsp;<button onClick={handleSubmit}>Delete</button>&nbsp;&nbsp;
                        <NavLink to={`/business/${singleReview.business_id}/edit`}>
                            <button>Edit</button>
                        </NavLink>
                    </div>}
                </div>
            </div>
            <div>
                {singleReview.review}
            </div>
            <div className="business-review-images">

                {singleReview.images.map(e => (
                    <img alt='review-photos' src={e?.review_image}></img>
                ))}
            </div>
        </div>
    )
}

export default BusinessReviews;
