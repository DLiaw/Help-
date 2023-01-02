import React, { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { getAllReviews } from '../../store/review'
import SingleReview from './SingleBusiness'
import './landingPage.css'

// Landing page components

const LandingPage = () => {
    const allReview = useSelector(state => Object.values(state.review.allReviews))
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getAllReviews())
    }, [dispatch])
    // if (!allReview) return null;
    let reviews = []
    if (allReview) {
        allReview.slice(0, 6).map(review => (
            reviews.push(<SingleReview key={review.id} review={review} />)
        ))
    } else { reviews = (<>failed</>) }
    return (
        <div className='single-card-flex'>
            <div className='title'> <h1 className='title-h1'>Recent Activity</h1></div>
            <div className='single-card-grid'>
                {reviews}
            </div>
        </div>
    )
}


export default LandingPage;
