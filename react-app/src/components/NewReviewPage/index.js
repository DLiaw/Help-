import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom';
import { newReview, addReviewImage } from '../../store/review';
import { getOneBusiness } from '../../store/business';
import StarRating from './StarRating';
import './NewReview.css'
import image1 from './image1.png'
import image2 from './image2.png'

const CreateReview = () => {
    const user = useSelector(state => state.session.user)
    const business = useSelector(state => state.business.oneBusiness)
    const dispatch = useDispatch()
    const history = useHistory()
    const [errors, setErrors] = useState({})
    const [review, setReview] = useState()
    const [stars, setStars] = useState()
    const [imageErrors, setImageErrors] = useState({})
    const [review_image, setReview_image] = useState('')
    const [errorsShow, setErrorsShown] = useState(false);

    const reviewImage = (e) => {
        const file = e.target.files[0];
        setReview_image(file);
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        setErrorsShown(true)
        const reviews = {
            review, stars, 'user_id': user.id, 'business_id': business.id
        }
        const reviewNew = await dispatch(newReview(reviews))

        if (reviewNew && !reviewNew.errors) {
            const data = new FormData()
            const review_id = reviewNew.id
            await data.append('image', review_image)
            await data.append('review_id', review_id)
            await dispatch(addReviewImage(data))
        }
        if (reviewNew.errors) setErrors(reviewNew.errors)
        if (!reviewNew.errors) history.push(`/business/${business.id}`)
    }

    return (
        <div className='create-review-main-div'>
            <div className='two-image-div'>
                <img className='review-form-image1' alt='review-img1' src={image1}></img>
            </div>
            <div className='reviw-form-star'>

                <div >
                    <div style={{ fontSize: '30px', paddingBottom: '5px' }}>{business.name}</div>
                    <form onSubmit={handleSubmit}>
                        <label style={{ paddingRight: '200px', color: 'grey', fontSize: '20px' }}>Your thoughts here...</label>
                        <textarea
                            className='review-form-input'
                            type="text"
                            placeholder="I ordered the Creme Brulee Boba Milk , with 75% sweetness. The drink had the right level of sweetness, and the boba itself was perfectly chewy. I wanted to try out their other toppings as well, such as Mochi and Agar Boba, however the..."
                            value={review}
                            onChange={(e) => { setReview(e.target.value); setImageErrors([]) }}
                            required />
                    </form>
                    {errors.review && (
                        <div className='errors'>{errors.review}</div>
                    )}
                    {errors.stars && (
                        <div className='errors'>{errors.stars}</div>
                    )}
                </div>
                <div className='reivew-input-main review-photo-input'>
                    <form>
                        <input
                            type="file"
                            accept="image/*"
                            onChange={reviewImage}
                        />
                    </form>
                    {errorsShow && imageErrors.length > 0 && (
                        <div className='errors'>{imageErrors[0]}</div>
                    )}
                </div>
                <div className='review-star-div' >
                    <div className='stars-div'>
                        <StarRating className='review-stars' setStars={setStars} stars={stars} value={stars} />
                    </div>
                    <div className='submit-button-div'>
                        <button className='review-submit-button' onClick={handleSubmit}>Submit</button>
                    </div>
                </div>
            </div>
            <div className='two-image-div'>
                <img className='review-form-image2' alt='review-img2' src={image2}></img>
            </div>
        </div>
    )
}

export default CreateReview;
