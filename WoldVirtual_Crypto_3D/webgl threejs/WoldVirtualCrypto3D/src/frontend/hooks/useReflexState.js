import { useEffect, useState } from 'react';
import { useReflex } from 'reflex-react'; // Assuming reflex-react is the package for Reflex integration

const useReflexState = () => {
    const [state, setState] = useState(null);
    const reflex = useReflex();

    useEffect(() => {
        const fetchState = async () => {
            try {
                const response = await reflex.get('/api/estado'); // Adjust the endpoint as necessary
                setState(response.data.scene_data);
            } catch (error) {
                console.error('Error fetching state from Reflex:', error);
            }
        };

        fetchState();
    }, [reflex]);

    const updateState = async (newState) => {
        try {
            await reflex.post('/api/update-scene', newState); // Adjust the endpoint as necessary
            setState(newState);
        } catch (error) {
            console.error('Error updating state in Reflex:', error);
        }
    };

    return [state, updateState];
};

export default useReflexState;