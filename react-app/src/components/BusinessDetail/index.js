import React, { useEffect, useRef, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { getOneBusiness } from '../../store/business';
import { getBusinessReviews } from '../../store/review'
import SingleBusiness from './SingleBusiness'
import BusinessReviews from './BusinessReviews'
import Navbar from './Nav.js'
import './businessDetail.css'
// Business details page

const BusinessDetail = () => {
    const [load, setLoad] = useState(false)
    const business = useSelector(state => state.business?.oneBusiness)
    const { id } = useParams();
    const dispatch = useDispatch()
    const reviews = useSelector(state => Object.values(state.review?.allReviews))
    const [scrollX, setscrollX] = useState(0);
    const [scrolEnd, setscrolEnd] = useState(false);
    const scrl = useRef()


    useEffect(async () => {
        await dispatch(getBusinessReviews(id))
        await dispatch(getOneBusiness(id))
        setLoad(true)
    }, [dispatch])

    useEffect(() => {

        if (
            scrl.current &&
            scrl?.current?.scrollWidth === scrl?.current?.offsetWidth
        ) {
            setscrolEnd(true);
        } else {
            setscrolEnd(false);
        }
        return () => { };
    }, [scrl?.current?.scrollWidth, scrl?.current?.offsetWidth]);

    const slide = (shift) => {
        scrl.current.scrollLeft += shift;
        setscrollX(scrollX + shift);
        if (
            Math.floor(scrl.current.scrollWidth - scrl.current.scrollLeft) <=
            scrl.current.offsetWidth
        ) {
            setscrolEnd(true);
        } else {
            setscrolEnd(false);
        }
    };

    const scrollCheck = () => {
        setscrollX(scrl.current.scrollLeft);
        if (
            Math.floor(scrl.current.scrollWidth - scrl.current.scrollLeft) <=
            scrl.current.offsetWidth
        ) {
            setscrolEnd(true);
        } else {
            setscrolEnd(false);
        }
    };

    if (!Object.values(business).length) return null;
    return load && (

        <div className='business-outer'>
            <Navbar business={business} />
            <div className='business-images business-snaps' ref={scrl} onScroll={scrollCheck}>
                <div className='business-gradient'>

                    <button className="prev scrollbtn" onClick={() => slide(-300)} >
                        <i class="fa-solid fa-angles-left"></i>
                    </button>


                    <button className="next scrollbtn" onClick={() => slide(+300)}>
                        <i class="fa-solid fa-angles-right"></i>
                    </button>
                </div>
                <div className='business-solo-image' >
                    {business.images?.map(e => (
                        <img className='business-img' alt="business-logo" src={e.business_image}></img>
                    ))}
                </div>
            </div>
            <div className='info-photo'>
                <div>
                    <SingleBusiness business={business} />
                </div>
                <div className='photo-button-div'>
                    <button className='photo-button'>See All Photos</button>
                </div>
            </div>
            <div className='review-business-info'>
                <div className='user-reviews'>
                    {reviews?.map(singleReview => (
                        <BusinessReviews key={singleReview.id} singleReview={singleReview} />
                    ))}
                </div>
                <div className='business-info'>
                    <div className='business-info-site' >
                        <a target="_blank" style={{ textDecoration: 'none', color: 'grey', wordBreak: 'break-all' }} href={business.site}>
                            {business.site}
                        </a>
                        <i class="fa-solid fa-location-arrow" />
                    </div>
                    <div className='business-info-phone'>
                        {business.phone_number}<i class="fa-solid fa-phone-volume" />
                    </div>
                    <div className='business-info-address'>
                        <div className='business-info-address-detail'>
                            {business.address}.&nbsp;{business.city}&nbsp;
                            {business.state},&nbsp;{business.zip}
                        </div>
                        <div>
                            <i class="fa-solid fa-location-dot" />
                        </div>
                    </div>
                </div>
            </div>
        </div>

    )

}

export default BusinessDetail;
