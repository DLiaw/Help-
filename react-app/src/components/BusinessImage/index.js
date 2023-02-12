import React, { useState, useEffect } from "react";
import { useHistory, useParams } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux';
import { addBusinessImage, getOneBusiness } from "../../store/business";
import SingleBusinessImage from './singleBusinessImage';
import './businessImage.css';


const UploadImage = () => {
    const dispatch = useDispatch()
    const { id } = useParams()
    const business = useSelector(state => state.business.oneBusiness)
    const [business_image, setBusiness_image] = useState('')

    useEffect(() => {
        if (!Object.values(business).length) dispatch(getOneBusiness(id))
    }, [dispatch, business])

    const updateImage = (e) => {
        const file = e.target.files[0];
        setBusiness_image(file);
    }

    const handleAddImages = (e) => {
        e.preventDefault()
        const data = new FormData()
        const business_id = business.id
        data.append('image', business_image)
        data.append('business_id', business_id)
        dispatch(addBusinessImage(data))
    }


    return (
        <div className="business-image-main-div">
            <h1>Manage your images...</h1>
            <div className="file-submit-div">
                <form>
                    <input
                        type="file"
                        accept="image/*"
                        onChange={updateImage}
                    />
                    <button onClick={handleAddImages} className="imgBtn" type="submit">Submit</button>
                </form>
            </div>
            <div className="singlePhotoImage">
                {business?.images?.map(image => (
                    < SingleBusinessImage key={image.id} image={image} />
                ))}
            </div>
        </div>
    )
}

export default UploadImage;
