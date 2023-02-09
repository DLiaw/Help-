import React, { useEffect, useRef, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams, NavLink } from 'react-router-dom';
import { getOneBusiness } from '../../store/business';
import { getBusinessReviews } from '../../store/review'
import SingleBusiness from './SingleBusiness'
import BusinessReviews from './BusinessReviews'
import MyGoogleMap from '../GoogleMaps';
import Navbar from './Nav.js'
import image from './image.png'
import './businessDetail.css'
// Business details page

const BusinessDetail = () => {
    const [load, setLoad] = useState(false)
    const user = useSelector(state => state.session.user)
    const business = useSelector(state => state.business?.oneBusiness)
    const { id } = useParams();
    const dispatch = useDispatch()
    const reviews = useSelector(state => Object.values(state.review?.allReviews))
    const [scrollX, setscrollX] = useState(0);
    const [scrolEnd, setscrolEnd] = useState(false);
    const scrl = useRef(null)


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
                    <button className="prev scrollbtn" onClick={() => slide(-300)}>
                        <i class="fa-solid fa-angles-left"></i>
                    </button>
                    <button className="next scrollbtn" onClick={() => slide(+300)}>
                        <i class="fa-solid fa-angles-right"></i>
                    </button>
                </div>
                <div className='business-solo-image' >
                    {business.images?.map(e => (
                        <img className='business-img' alt="business-logo" src={e.business_image} onError={e => { e.currentTarget.src = 'https://www.drupal.org/files/project-images/broken-image.jpg' }}></img>
                    ))}
                </div>
            </div>
            <div className='info-photo'>
                <div >
                    <SingleBusiness business={business} />
                </div>
                {business.owner_id == user.id && <div className='photo-button-div'>
                    <NavLink className='photo-button' style={{ textDecoration: 'none' }} to={`/business/${id}/images`} >Add Photos</NavLink>
                </div>}
            </div>
            <div className='review-business-info'>
                <div className='user-reviews'>
                    <div className='business-hour-image'>
                        <div className='business-image'>
                            <img alt='business-hours' src={image}></img>
                        </div>
                        <div className='business-open-close'>
                            <div className='hours-by-day'>
                                &nbsp;Mon&nbsp;&nbsp; {business.monOpen}&nbsp;&nbsp;-&nbsp;&nbsp;{business.monClose}
                            </div>
                            <div className='hours-by-day'>
                                &nbsp;Tue&nbsp;&nbsp;&nbsp; {business.tueOpen}&nbsp;&nbsp;-&nbsp;&nbsp;{business.tueClose}
                            </div>
                            <div className='hours-by-day'>
                                &nbsp;Wed&nbsp;&nbsp; {business.wedOpen}&nbsp;&nbsp;-&nbsp;&nbsp;{business.wedClose}
                            </div>
                            <div className='hours-by-day'>
                                &nbsp;Thu&nbsp;&nbsp;&nbsp; {business.thuOpen}&nbsp;&nbsp;-&nbsp;&nbsp;{business.thuClose}
                            </div>
                            <div className='hours-by-day'>
                                &nbsp;Fri&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {business.friOpen}&nbsp;&nbsp;-&nbsp;&nbsp;{business.friClose}
                            </div>
                            <div className='hours-by-day'>
                                &nbsp;Sat&nbsp;&nbsp;&nbsp;&nbsp; {business.satOpen}&nbsp;&nbsp;-&nbsp;&nbsp;{business.satClose}
                            </div>
                            <div className='hours-by-day'>
                                &nbsp;Sun&nbsp;&nbsp;&nbsp; {business.sunOpen}&nbsp;&nbsp;-&nbsp;&nbsp;{business.sunClose}
                            </div>
                        </div>
                    </div>
                    <div>
                        {reviews?.map(singleReview => (
                            <BusinessReviews key={singleReview.id} singleReview={singleReview} />
                        ))}
                    </div>
                </div>
                <div className='business-info-maps'>
                    <div className='business-info'>
                        <div className='business-info-site' >
                            <a target="_blank" style={{ textDecoration: 'none', color: 'grey', wordBreak: 'break-all', textOverflow: 'ellipsis' }} href={business.site}>
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
                    <div className='business-map'>
                        <MyGoogleMap business={business} />
                    </div>
                </div>
            </div>
        </div>

    )

}

export default BusinessDetail;
