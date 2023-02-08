import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { deleteBusinessImage, cleanupBusiness } from "../../store/business";
import './businessImage.css'


const SingleBusinessImage = ({ image }) => {
    const [open, setOpen] = useState(false)
    const dispatch = useDispatch()

    const handleDelete = async (e) => {
        e.preventDefault()
        await dispatch(deleteBusinessImage(image.id))
        await dispatch(cleanupBusiness())
    }

    return (
        <div className='single-photo-drop'>
            <div>
                <img id='businessPhoto' alt="businessPhoto" src={image?.business_image}></img>
            </div>
            <div className="ellipsis-div">
                <i onClick={() => setOpen(!open)} style={{ cursor: 'pointer' }} class="fa-solid fa-ellipsis" />
            </div>
            {open && <Drop />}
        </div>
    )

    function Drop() {
        return (
            <div className="booking-delete" >
                <button className="deleteBtn imgBtn" onClick={handleDelete}>Delete</button>
            </div >
        )
    }
}

export default SingleBusinessImage;
